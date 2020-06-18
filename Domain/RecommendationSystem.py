import sqlite3
from time import time

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from IPython.display import display

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer


class RecommendationSystem:

    def __init__(self):
        pass


football_data = sqlite3.connect('database.sqlite')
# Fetching required data tables
player_df = pd.read_sql("SELECT * FROM Player;", football_data)
player_stats_df = pd.read_sql("SELECT * FROM Player_Attributes;", football_data)
team_df = pd.read_sql("SELECT * FROM Team;", football_data)
team_stats_df = pd.read_sql("SELECT * FROM Team_Attributes;", football_data)
match_df = pd.read_sql_query("SELECT *  From Match ", football_data)

# Reduce match data to fulfill run time requirements
rows = ["country_id", "league_id", "season", "stage", "date", "match_api_id", "home_team_api_id",
        "away_team_api_id", "home_team_goal", "away_team_goal", "home_player_1", "home_player_2",
        "home_player_3", "home_player_4", "home_player_5", "home_player_6", "home_player_7",
        "home_player_8", "home_player_9", "home_player_10", "home_player_11", "away_player_1",
        "away_player_2", "away_player_3", "away_player_4", "away_player_5", "away_player_6",
        "away_player_7", "away_player_8", "away_player_9", "away_player_10", "away_player_11"]
match_df.dropna(subset=rows, inplace=True)
match_data = match_df.tail(1500)


# features functions
def get_last_matches(matches, date, team, x=5):
    ''' Get the last x matches of a given team. '''

    # Filter team matches from matches
    team_matches = matches[(matches['home_team_api_id'] == team) | (matches['away_team_api_id'] == team)]

    # Filter x last matches from team matches
    last_matches = team_matches[team_matches.date < date].sort_values(by='date', ascending=False).iloc[0:x, :]

    # Return last matches
    return last_matches


def get_last_matches_against_eachother(matches, date, home_team, away_team, x=5):
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
    ''' Get the goals of a specfic team from a set of matches. '''

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.home_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.away_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    # Return total goals
    return total_goals


def get_goals_conceided(matches, team):
    ''' Get the goals conceided of a specfic team from a set of matches. '''

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.away_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.home_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    # Return total goals
    return total_goals


def get_wins(matches, team):
    ''' Get the number of wins of a specfic team from a set of matches. '''

    # Find home and away wins
    home_wins = int(matches.home_team_goal[
                        (matches.home_team_api_id == team) & (matches.home_team_goal > matches.away_team_goal)].count())
    away_wins = int(matches.away_team_goal[
                        (matches.away_team_api_id == team) & (matches.away_team_goal > matches.home_team_goal)].count())

    total_wins = home_wins + away_wins

    # Return total wins
    return total_wins


def get_buildUp_stats(teams, team, date, x=1):
    ''' Get the last x matches of a given team. '''
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
    ''' Get the last x matches of a given team. '''
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
    ''' Get the last x matches of a given team. '''
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


def get_match_features(match, matches, teams, x=10):
    ''' Create match specific features for a given match. '''

    # Define variables
    date = match.date
    home_team = match.home_team_api_id
    away_team = match.away_team_api_id

    # Get last x matches of home and away team
    matches_home_team = get_last_matches(matches, date, home_team, x=4)
    matches_away_team = get_last_matches(matches, date, away_team, x=4)

    # Get last x matches of both teams against each other
    last_matches_against = get_last_matches_against_eachother(matches, date, home_team, away_team, x=3)

    # Create goal variables
    home_goals = get_goals(matches_home_team, home_team)
    away_goals = get_goals(matches_away_team, away_team)
    home_goals_conceided = get_goals_conceided(matches_home_team, home_team)
    away_goals_conceided = get_goals_conceided(matches_away_team, away_team)

    # Create team stats variables
    home_buildUp_stats = get_buildUp_stats(teams, home_team, date)
    away_buildUp_stats = get_buildUp_stats(teams, away_team, date)
    home_chanceCreation_stats = get_chance_creation_stats(teams, home_team, date)
    away_chanceCreation_stats = get_chance_creation_stats(teams, away_team, date)
    home_defense_stats = get_defense_stats(teams, home_team, date)
    away_defense_stats = get_defense_stats(teams, away_team, date)
    home_overall_stats = home_buildUp_stats + home_chanceCreation_stats + home_defense_stats
    away_overall_stats = away_buildUp_stats + away_chanceCreation_stats + away_defense_stats

    # Define result data frame
    result = pd.DataFrame()

    # Define ID features
    result.loc[0, 'match_api_id'] = match.match_api_id
    # result.loc[0, 'league_id'] = match.league_id

    # Create match features
    result.loc[0, 'home_team_goals_difference'] = home_goals - home_goals_conceided
    result.loc[0, 'away_team_goals_difference'] = away_goals - away_goals_conceided
    result.loc[0, 'games_won_home_team'] = get_wins(matches_home_team, home_team)
    result.loc[0, 'games_won_away_team'] = get_wins(matches_away_team, away_team)
    result.loc[0, 'games_against_won'] = get_wins(last_matches_against, home_team)
    result.loc[0, 'games_against_lost'] = get_wins(last_matches_against, away_team)
    result.loc[0, 'home_buildUp_stats'] = home_buildUp_stats
    result.loc[0, 'away_buildUp_stats'] = away_buildUp_stats
    result.loc[0, 'home_chanceCreation_stats'] = home_chanceCreation_stats
    result.loc[0, 'away_chanceCreation_stats'] = away_chanceCreation_stats
    result.loc[0, 'home_defense_stats'] = home_defense_stats
    result.loc[0, 'away_defense_stats'] = away_defense_stats
    result.loc[0, 'home_overall_stats'] = home_overall_stats
    result.loc[0, 'away_overall_stats'] = away_overall_stats

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


def create_features(matches, teams, x=10, verbose=True):
    ''' Create and aggregate features and labels for all matches. '''

    if verbose is True:
        print("Generating match features...")
    start = time()

    # Get match features for all matches
    match_stats = matches.apply(lambda x: get_match_features(x, matches, teams, x=10), axis=1)

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
    labels = match_df.apply(get_match_label, axis=1)
    end = time()
    if verbose is True:
        print("Match labels generated in {:.1f} minutes".format((end - start) / 60))

    # Merges features and labels into one frame
    features = pd.merge(match_stats, labels, on='match_api_id', how='left')

    # Drop NA values
    features.dropna(inplace=True)

    # Return preprocessed data
    return features


features = create_features(match_data, team_stats_df)
cols = features.columns.tolist()
display(features.head())
display(cols)

# Separate into feature set and target variable
# FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
X_all = features.drop(['label'], 1)
X_all = X_all.drop(['match_api_id'], 1)
# display(X_all.columns.tolist())
y_all = features['label']

# Standardising the data.

# Center to the mean and component wise scale to unit variance.
cols = [['home_team_goals_difference', 'away_team_goals_difference', 'games_won_home_team', 'games_won_away_team',
         'games_against_won', 'games_against_lost', 'home_buildUp_stats', 'away_buildUp_stats',
         'home_chanceCreation_stats', 'away_chanceCreation_stats', 'home_defense_stats', 'away_defense_stats',
         'home_overall_stats', 'away_overall_stats']]
for col in cols:
    X_all[col] = scale(X_all[col])

print("\nFeature values:")
display(X_all.head())

# Shuffle and split the dataset into training and testing set.
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y_all)


# F1 score (also F-score or F-measure) is a measure of a test's accuracy.
# It considers both the precision p and the recall r of the test to compute
# the score: p is the number of correct positive results divided by the number of
# all positive results, and r is the number of correct positive results divided by
# the number of positive results that should have been returned. The F1 score can be
# interpreted as a weighted average of the precision and recall, where an F1 score
# reaches its best value at 1 and worst at 0.


def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''

    # Start the clock, train the classifier, then stop the clock
    start = time()
    clf.fit(X_train, y_train)
    end = time()

    # Print the results
    print("Trained model in {:.4f} seconds".format(end - start))


def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''

    # Start the clock, make predictions, then stop the clock
    start = time()
    y_pred = clf.predict(features)

    end = time()
    # Print and return results
    print("Made predictions in {:.4f} seconds.".format(end - start))

    return f1_score(target, y_pred, labels=['Win', 'Draw', 'Lose'], average='micro'), sum(target == y_pred) / float(len(y_pred))


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''

    # Indicate the classifier and the training set size
    print("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))

    # Train the classifier
    train_classifier(clf, X_train, y_train)

    # Print the results of prediction for both training and testing
    f1, acc = predict_labels(clf, X_train, y_train)
    print(f1, acc)
    print("F1 score and accuracy score for training set: {:.4f} , {:.4f}.".format(f1, acc))

    f1, acc = predict_labels(clf, X_test, y_test)
    print("F1 score and accuracy score for test set: {:.4f} , {:.4f}.".format(f1, acc))


# Initialize the three models (XGBoost is initialized later)
clf_A = LogisticRegression(random_state=42, multi_class="multinomial")
clf_B = SVC(random_state=912, kernel='rbf')
# Boosting refers to this general problem of producing a very accurate prediction rule
# by combining rough and moderately inaccurate rules-of-thumb
clf_C = xgb.XGBClassifier(max_depth=4, objective='multi:softmax', n_estimators=150)
# RF_clf = RandomForestClassifier(n_estimators=200, random_state=1, class_weight='balanced')
# GNB_clf = GaussianNB()

train_predict(clf_A, X_train, y_train, X_test, y_test)
print('')
train_predict(clf_B, X_train, y_train, X_test, y_test)
print('')
train_predict(clf_C, X_train, y_train, X_test, y_test)
print('')
# train_predict(RF_clf, X_train, y_train, X_test, y_test)
# print('')
# train_predict(GNB_clf, X_train, y_train, X_test, y_test)
# print('')

# tuning in XGBoost
parameters = {'learning_rate': [0.1],
              'n_estimators': [40],
              'max_depth': [3],
              'min_child_weight': [3],
              'gamma': [0.4],
              'subsample': [0.8],
              'colsample_bytree': [0.8],
              'reg_alpha': [1e-5]
              }
clf = xgb.XGBClassifier(seed=2)

# Make an f1 scoring function using 'make_scorer'
f1_scorer = make_scorer(f1_score, labels=['Win', 'Draw', 'Lose'], average='micro')

# Perform grid search on the classifier using the f1_scorer as the scoring method
grid_obj = GridSearchCV(clf,
                        scoring=f1_scorer,
                        param_grid=parameters,
                        cv=5)

# Fit the grid search object to the training data and find the optimal parameters
grid_obj = grid_obj.fit(X_train, y_train)

# Get the estimator
clf = grid_obj.best_estimator_
print(clf)

# Report the final F1 score for training and testing after parameter tuning
f1, acc = predict_labels(clf, X_train, y_train)
print("F1 score and accuracy score for training set: {:.4f} , {:.4f}.".format(f1, acc))

f1, acc = predict_labels(clf, X_test, y_test)
print("F1 score and accuracy score for test set: {:.4f} , {:.4f}.".format(f1, acc))
