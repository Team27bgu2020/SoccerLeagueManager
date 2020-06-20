import sqlite3
from time import time
import pandas as pd
from sklearn.preprocessing import scale
from IPython.display import display


def prepare_RS_data(database_path, prepared_data_path):

    football_data = sqlite3.connect(database_path)
    # Fetching required data tables
    player_df = pd.read_sql("SELECT * FROM Player;", football_data)
    player_stats_df = pd.read_sql("SELECT * FROM Player_Attributes Where date < '2015-07-01';", football_data)
    player_stats_df.dropna(inplace=True)
    test_player_stats_df = pd.read_sql("SELECT * FROM Player_Attributes", football_data)
    test_player_stats_df.dropna(inplace=True)
    team_df = pd.read_sql("SELECT * FROM Team;", football_data)
    team_stats_df = pd.read_sql("SELECT * FROM Team_Attributes Where date < '2015-07-01';", football_data)
    team_stats_df.dropna(inplace=True)
    test_team_stats_df = pd.read_sql("SELECT * FROM Team_Attributes Where date >= '2015-07-01';", football_data)
    test_team_stats_df.dropna(inplace=True)
    match_df = pd.read_sql_query("SELECT *  From Match", football_data)

    # Reduce match data to fulfill run time requirements
    rows = ["country_id", "league_id", "season", "stage", "date", "match_api_id", "home_team_api_id",
            "away_team_api_id", "home_team_goal", "away_team_goal", "home_player_1", "home_player_2",
            "home_player_3", "home_player_4", "home_player_5", "home_player_6", "home_player_7",
            "home_player_8", "home_player_9", "home_player_10", "home_player_11", "away_player_1",
            "away_player_2", "away_player_3", "away_player_4", "away_player_5", "away_player_6",
            "away_player_7", "away_player_8", "away_player_9", "away_player_10", "away_player_11"]
    match_df.dropna(subset=rows, inplace=True)
    match_data = match_df


    # prepare train set
    print('preparing train set')
    features = create_features(match_data, team_stats_df, player_stats_df)
    features = features.drop(['match_api_id'], 1)

    # Center to the mean and component wise scale to unit variance.
    cols = [['home_team_goals_difference', 'away_team_goals_difference', 'games_won_home_team', 'games_won_away_team',
             'games_against_won', 'games_against_lost', 'home_buildUp_stats', 'away_buildUp_stats',
             'home_chanceCreation_stats', 'away_chanceCreation_stats', 'home_defense_stats', 'away_defense_stats',
             'home_overall_stats', 'away_overall_stats', 'home_players_rank', 'away_players_rank']]
    for col in cols:
        features[col] = scale(features[col])

    print("\nFeature values:")
    display(features.head())

    features.to_csv(prepared_data_path)

def create_features(matches, teams, players, x=10, verbose=True):
    ''' Create and aggregate features and labels for all matches. '''

    if verbose is True:
        print("Generating match features...")
    start = time()

    # Get match features for all matches
    match_stats = matches.apply(lambda x: get_match_features(x, matches, teams, players, x=10), axis=1)

    # Create dummies for league ID feature
    # dummies = pd.get_dummies(match_stats['league_id']).rename(columns=lambda x: 'League_' + str(x))
    # match_stats = pd.concat([match_stats, dummies], axis=1)
    # match_stats.drop(['league_id'], inplace=True, axis=1)

    end = time()
    if verbose is True:
        print("Match features generated in {:.1f} minutes".format((end - start) / 60))

    if verbose is True:
        print("Generating match labels...")
    start = time()

    # Create match labels
    labels = matches.apply(get_match_label, axis=1)
    end = time()
    if verbose is True:
        print("Match labels generated in {:.1f} minutes".format((end - start) / 60))

    # Merges features and labels into one frame
    features = pd.merge(match_stats, labels, on='match_api_id', how='left')

    # Drop NA values
    features.dropna(inplace=True)

    # Return preprocessed data
    return features


def get_match_features(match, matches, teams, players, x=10):
    ''' Create match specific features for a given match. '''

    # Define variables
    date = match.date
    home_team = match.home_team_api_id
    away_team = match.away_team_api_id

    # Get last x matches of home and away team
    matches_home_team = get_last_matches(matches, date, home_team, x=4)
    matches_away_team = get_last_matches(matches, date, away_team, x=4)

    # Get team players for match
    home_team_players = get_home_team_players(match)
    away_team_players = get_away_team_players(match)

    # Get last x matches of both teams against each other
    last_matches_against = get_last_matches_against_eachother(matches, date, home_team, away_team, x=3)

    # Create goal variables
    home_goals = get_goals(matches_home_team, home_team)
    away_goals = get_goals(matches_away_team, away_team)
    home_goals_conceded = get_goals_conceded(matches_home_team, home_team)
    away_goals_conceded = get_goals_conceded(matches_away_team, away_team)

    # Create team stats variables
    home_build_up_stats = get_buildUp_stats(teams, home_team, date)
    away_build_up_stats = get_buildUp_stats(teams, away_team, date)
    home_chance_creation_stats = get_chance_creation_stats(teams, home_team, date)
    away_chance_creation_stats = get_chance_creation_stats(teams, away_team, date)
    home_defense_stats = get_defense_stats(teams, home_team, date)
    away_defense_stats = get_defense_stats(teams, away_team, date)
    home_overall_stats = home_build_up_stats + home_chance_creation_stats + home_defense_stats
    away_overall_stats = away_build_up_stats + away_chance_creation_stats + away_defense_stats
    home_team_players_ranking = get_team_players_rating(home_team_players, players, date)
    away_team_players_ranking = get_team_players_rating(away_team_players, players, date)

    # Define result data frame
    result = pd.DataFrame()

    # Define ID features
    result.loc[0, 'match_api_id'] = match.match_api_id
    # result.loc[0, 'league_id'] = match.league_id

    # Create match features
    result.loc[0, 'home_team_goals_difference'] = home_goals - home_goals_conceded
    result.loc[0, 'away_team_goals_difference'] = away_goals - away_goals_conceded
    result.loc[0, 'games_won_home_team'] = get_wins(matches_home_team, home_team)
    result.loc[0, 'games_won_away_team'] = get_wins(matches_away_team, away_team)
    result.loc[0, 'games_against_won'] = get_wins(last_matches_against, home_team)
    result.loc[0, 'games_against_lost'] = get_wins(last_matches_against, away_team)
    result.loc[0, 'diff_buildUp_stats'] = home_build_up_stats - away_build_up_stats
    result.loc[0, 'diff_chanceCreation_stats'] = home_chance_creation_stats - away_chance_creation_stats
    result.loc[0, 'diff_defense_stats'] = home_defense_stats - away_defense_stats
    result.loc[0, 'diff_overall_stats'] = home_overall_stats - away_overall_stats
    result.loc[0, 'home_players_rank'] = home_team_players_ranking
    result.loc[0, 'away_players_rank'] = away_team_players_ranking
    result.loc[0, 'date'] = date

    # Return match features
    return result.loc[0]


def get_match_label(match):
    ''' Derives a label for a given match. '''

    # Define variables
    home_goals = match['home_team_goal']
    away_goals = match['away_team_goal']
    label = pd.DataFrame()
    label.loc[0, 'match_api_id'] = match['match_api_id']

    # Identify match label
    if home_goals > away_goals:
        label.loc[0, 'label'] = "Win"
        # FTR[match['id'] - 1] = ("Win")
    if home_goals == away_goals:
        label.loc[0, 'label'] = "Draw"
        # FTR[match['id'] - 1] = ("Draw")
    if home_goals < away_goals:
        label.loc[0, 'label'] = "Lose"
        # FTR[match['id'] - 1] = ("Lose")

    # Return label
    return label.loc[0]


# features functions
def get_last_matches(matches, date, team, x=3):
    ''' Get the last x matches of a given team. '''

    # Filter team matches from matches
    team_matches = matches[(matches['home_team_api_id'] == team) | (matches['away_team_api_id'] == team)]

    # Filter x last matches from team matches
    last_matches = team_matches[team_matches.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]

    # Return last matches
    return last_matches


def get_last_matches_against_eachother(matches, date, home_team, away_team, x=3):
    ''' Get the last x matches of two given teams. '''

    # Find matches of both teams
    home_matches = matches[(matches['home_team_api_id'] == home_team) & (matches['away_team_api_id'] == away_team)]
    away_matches = matches[(matches['home_team_api_id'] == away_team) & (matches['away_team_api_id'] == home_team)]
    total_matches = pd.concat([home_matches, away_matches])

    # Get last x matches
    try:
        last_matches = total_matches[total_matches.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]
    except:
        last_matches = total_matches[total_matches.date < date].sort_values(by='date', ascending=False).iloc[
                       0:total_matches.shape[0], :]

        # Check for error in data
        if last_matches.shape[0] > x:
            print("Error in obtaining matches")

    # Return data
    return last_matches


def get_goals(matches, team):
    ''' Get the goals of a specific team from a set of matches. '''

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.home_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.away_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    # Return total goals
    return total_goals


def get_goals_conceded(matches, team):
    ''' Get the goals conceded of a specific team from a set of matches. '''

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.away_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.home_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    # Return total goals
    return total_goals


def get_wins(matches, team):
    ''' Get the number of wins of a specific team from a set of matches. '''

    # Find home and away wins
    home_wins = int(matches.home_team_goal[
                        (matches.home_team_api_id == team) & (matches.home_team_goal > matches.away_team_goal)].count())
    away_wins = int(matches.away_team_goal[
                        (matches.away_team_api_id == team) & (matches.away_team_goal > matches.home_team_goal)].count())

    total_wins = home_wins + away_wins

    # Return total wins
    return total_wins


def get_buildUp_stats(teams, team, date, x=1):
    ''' Get the build up stats of a given team. '''
    overall_stats = 0
    # Filter team from teams
    team_stats = teams[(teams['team_api_id'] == team)]

    # Filter x last forms from teams stats
    last_play = team_stats[team_stats.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]
    try:
        play_speed = int(last_play.buildUpPlaySpeed)
        overall_stats += play_speed
    except:
        overall_stats += 40
    try:
        play_dribble = int(last_play.buildUpPlayDribbling)
        overall_stats += play_dribble
    except:
        overall_stats += 40
    try:
        play_pass = int(last_play.buildUpPlayPassing)
        overall_stats += play_pass
    except:
        overall_stats += 40
    # Return last matches
    return overall_stats


def get_chance_creation_stats(teams, team, date, x=1):
    ''' Get the chance creation stats of a given team. '''
    overall_stats = 0
    # Filter team from teams
    team_stats = teams[(teams['team_api_id'] == team)]

    # Filter x last forms from teams stats
    last_play = team_stats[team_stats.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]
    try:
        passing = int(last_play.chanceCreationPassing)
        overall_stats += passing
    except:
        overall_stats += 40
    try:
        crossing = int(last_play.chanceCreationCrossing)
        overall_stats += crossing
    except:
        overall_stats += 40
    try:
        shooting = int(last_play.chanceCreationShooting)
        overall_stats += shooting
    except:
        overall_stats += 40
    # Return last matches
    return overall_stats


def get_defense_stats(teams, team, date, x=1):
    ''' Get the defense stats of a given team. '''
    overall_stats = 0
    # Filter team from teams
    team_stats = teams[(teams['team_api_id'] == team)]

    # Filter x last forms from teams stats
    last_play = team_stats[team_stats.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]
    try:
        pressure = int(last_play.defencePressure)
        overall_stats += pressure
    except:
        overall_stats += 35
    try:
        aggression = int(last_play.defenceAggression)
        overall_stats += aggression
    except:
        overall_stats += 40
    try:
        team_width = int(last_play.defenceTeamWidth)
        overall_stats += team_width
    except:
        overall_stats += 40
    # Return last matches
    return overall_stats


def get_team_players_rating(team_players, players, date):

    team_players_rank_sum = 0
    players_num = len(team_players)

    for player_id in team_players:
        try:
            player_stats = players[(players['player_api_id'] == player_id)]
            most_updated_stats = player_stats[player_stats.date < date].sort_values(by='date', ascending=False).iloc[0:1, :]
            player_rank = int(most_updated_stats['overall_rating'])
            team_players_rank_sum += player_rank
        except Exception as err:
            # print(err)
            players_num -= 1

    return team_players_rank_sum/players_num


def get_home_team_players(match):

    players = []

    for i in range(1, 12):
        attr = 'home_player_' + str(i)
        players.append(match[attr])

    return players


def get_away_team_players(match):
    players = []

    for i in range(1, 12):
        attr = 'away_player_' + str(i)
        players.append(match[attr])

    return players


prepare_RS_data("C:\\Users\\sfrei\\Desktop\\Degree\\Y03S02\\Project Preparation\\database.sqlite", "C:\\Users\\sfrei\\Desktop\\Degree\\Y03S02\\Project Preparation\\Part 5\\'small_data.csv")