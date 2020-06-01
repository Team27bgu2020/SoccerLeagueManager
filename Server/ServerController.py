import json

from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from Server import Server
from Service.MatchController import MatchController
from Service.SignedUserController import SignedUserController
from Service.LeagueController import LeagueController
from Service.TeamManagementController import TeamManagementController
from Service.NotificationsController import NotificationController

from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoPolicyDB import MongoPolicyDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB

from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum

import datetime as date
import csv

""" This class is the controller that connects the server to the Domain """

users_db = MongoUserDB()
team_db = MongoTeamDB()
policy_db = MongoPolicyDB()
league_db = MongoLeagueDB()
season_db = MongoSeasonDB()
game_db = MongoGameDB()
game_event_db = MongoGameEventDB()
league_controller = LeagueController(league_db, season_db, users_db, policy_db)
signed_user_controller = SignedUserController(users_db)
notification_controller = NotificationController(users_db, game_db)
team_management_controller = TeamManagementController(team_db, users_db)
match_controller = MatchController(game_db, users_db, game_event_db, team_db)
if not signed_user_controller.confirm_user('dor', '1234'):
    signed_user_controller.add_system_admin('dor', '1234', 'dor', date.datetime(1994, 1, 20))

try:
    signed_user_controller.add_team_owner('shahar', '1234', 'shahar', date.datetime(1993, 1, 1))
    signed_user_controller.add_referee(RefereeQualificationEnum.MAIN, 'oscar', '1234', 'oscar', date.datetime(1994, 11, 9))
    main_referee = signed_user_controller.get_user_by_name('oscar')
    owner = signed_user_controller.get_user_by_name('shahar')

    team_management_controller.open_new_team('Brca', owner.user_id)
    team_management_controller.open_new_team('Real', owner.user_id)

    match_controller.add_game('Brca', 'Real', date.datetime.now(), 'S', main_referee.user_id)
    match_controller.start_game(game_db.get_id_counter() -1)

except Exception:
    pass
# user = signed_user_controller.get_user('dor')
# user.notify('hello 1')
# user.notify('hello 2')
# user.notify('hello 3')


def user_login(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    if not signed_user_controller.confirm_user(user_name, password):
        return 'Error'
    else:
        user = signed_user_controller.get_user_by_name(user_name)
        if str(type(user)).split('.')[1] == 'TeamUser':
            return {
                'user_name': user_name,
                'user_type': str(type(user.role)).split('.')[1]
            }
        else:
            return {
                'user_name': user_name,
                'user_type': str(type(user)).split('.')[1],
            }


def user_register(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    role = mess_info['data']['role']
    try:
        if signed_user_controller.get_user_by_name(user_name) is not None:
            return 'Username Error'
    except:
        try:
            if role == 'Fan':
                signed_user_controller.add_fan(user_name, password, name,
                                               date.datetime.strptime(birth_date, '%Y-%m-%d'))
            elif role == "Team Owner":
                signed_user_controller.add_team_owner(user_name, password, name,
                                                      date.datetime.strptime(birth_date, '%Y-%m-%d'))
            elif role == 'Union Representor':
                signed_user_controller.add_union_representor(user_name, password, name,
                                                             date.datetime.strptime(birth_date, '%Y-%m-%d'))
            elif role == 'System Admin':
                signed_user_controller.add_system_admin(user_name, password, name,
                                                        date.datetime.strptime(birth_date, '%Y-%m-%d'))
            elif role == 'Referee':
                signed_user_controller.add_referee(RefereeQualificationEnum.REGULAR, user_name, password, name, date.datetime.strptime(birth_date, '%Y-%m-%d'))

            elif role == 'Main Referee':
                signed_user_controller.add_referee(RefereeQualificationEnum.MAIN, user_name, password, name, date.datetime.strptime(birth_date, '%Y-%m-%d'))
            else:
                return 'Error'
        except Exception:
            return 'Error'
        if str(type(signed_user_controller.get_user_by_name(user_name))).split('.')[1] == 'TeamUser':
            return {
                'user_name': user_name,
                'user_type': str(type(signed_user_controller.get_user_by_name(user_name).role)).split('.')[1]
            }
        else:
            return {
                'user_name': user_name,
                'user_type': str(type(signed_user_controller.get_user_by_name(user_name))).split('.')[1]
            }


def ref_register(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    qualification = RefereeQualificationEnum(mess_info['data']['qualification'])
    try:
        if signed_user_controller.get_user_by_name(user_name) is not None:
            return 'Username Error'
    except:
        try:
            signed_user_controller.add_referee(qualification, user_name, password, name,
                                               date.datetime.strptime(birth_date, '%Y-%m-%d'))
            return confirmation_massage()
        except Exception:
            return 'Error'


def remove_user(mess_info):
    user_name = mess_info['data']['user_name']
    try:
        if signed_user_controller.get_user_by_name(user_name) is not None:
            user_id = signed_user_controller.get_user_by_name(user_name).user_id
            signed_user_controller.delete_signed_user(user_id)
            return 'Success'
    except:
        return 'Error'


def get_user_info(mess_info):
    """ Change implementation """
    return {
        'user name': 'Dor123',
        'first name': 'Dor',
        'last name': 'Pinhas'
    }


def update_user_info(mess_info):
    user_id = mess_info['user_id']
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    try:
        signed_user_controller.edit_personal_data(signed_user_controller.get_user_by_name(user_id).user_id,
                                                  user_name, password, name,
                                                  date.datetime.strptime(birth_date, '%Y-%m-%d'))
        return confirmation_massage()
    except Exception:
        return 'Error'


def get_user_notifications(mess_info):
    user_name = mess_info['user_id']
    try:
        user = signed_user_controller.get_user_by_name(user_name)
        return {
            'user_name': user_name,
            'user_notifications': notification_controller.check_user_notifications(user)
        }
    except Exception as err:
        return 'Error'


def get_logs(mess_info):
    people = []
    reader = csv.reader(open('../Service/Event_Log.txt'), delimiter='\n')
    for row in reader:
        people.append(row)
    return people


def add_policy(mess_info):
    policy_type = mess_info['data']['policy_type']
    if policy_type == 'points':
        points_win = mess_info['data']['pointsWin']
        points_draw = mess_info['data']['pointsDraw']
        points_lose = mess_info['data']['pointsLose']
        try:
            league_controller.create_points_policy(points_win, points_draw, points_lose)
        except:
            return 'Error policy exists'
    elif policy_type == 'games':
        game_against_each_team = mess_info['data']['game_against_each_team']
        games_per_week = mess_info['data']['games_per_week']
        stadium = mess_info['data']['stadium']
        if stadium == 'Random Stadium':
            games_policy_enum = GameAssigningPoliciesEnum('Random')
        elif stadium == 'Home & Away Stadiums':
            games_policy_enum = GameAssigningPoliciesEnum('Equal')
        else:
            return 'Error'
        try:
            league_controller.create_game_schedule_policy(int(game_against_each_team), int(games_per_week), games_policy_enum)
        except:
            return 'Error policy exists'
    elif policy_type == 'budget':
        min_budget = mess_info['data']['min_budget']
        try:
            league_controller.create_team_budget_policy(min_budget)
        except:
            return 'Error policy exists'


def get_policy(mess_info):
    policy_type = mess_info['data']
    if policy_type == 'Budget':
        policies = league_controller.get_all_budget_policies()
        policies_final = []
        for policy in policies:
            poli = {
                'Policy ID': str(policy._TeamBudgetPolicy__policy_id),
                'Min Amount': policy.min_amount,
            }
            policies_final.append(poli)
        return policies_final
    if policy_type == 'Points':
        policies = league_controller.get_all_points_policies()
        policies_final = []
        for policy in policies:
            poli = {
                'Policy ID': str(policy._PointsCalculationPolicy__policy_id),
                'Win Points': policy.win_points,
                'Draw Points': policy.tie_points,
                'Lose Points': policy.lose_points,
            }
            policies_final.append(poli)
        return policies_final
    if policy_type == 'Games':
        policies = league_controller.get_all_schedule_policies()
        policies_final = []
        for policy in policies:
            poli = {
                'Policy ID': str(policy._GameSchedulePolicy__policy_id),
                'Games against each team': str(policy.team_games_num),
                'Games per week': str(policy.games_per_week),
                'Stadium': str(policy.games_stadium_assigning_policy).split('.')[1]
            }
            policies_final.append(poli)
        return policies_final


def add_team(mess_info):
    team_name = mess_info['data']['team_name']
    user = mess_info['user_id']
    try:
        team_management_controller.open_new_team(team_name, signed_user_controller.get_user_by_name(user).user_id)
    except:
        return 'Error'

def get_on_going_games(mess_info):
    referee_name = mess_info['user_id']
    try:
        referee = signed_user_controller.get_user_by_name(referee_name)
        all_on_going_game = match_controller.show_ongoing_games_by_referee(referee.user_id)
        all_games_final = []
        for game in all_on_going_game:
            game_dict = {
                'game_id': game.game_id,
                'home_team': game.home_team,
                'away_team': game.away_team
            }
            all_games_final.append(game_dict)
        return all_games_final
    except Exception as err:
        return str(err)

def add_event(mess_info):
    try:
        referee_name = mess_info['data']['referee_id']
        referee = signed_user_controller.get_user_by_name(referee_name)
        referee_id = int(referee.user_id)
        game_id = int(mess_info['data']['game_id'])
        event_type = mess_info['data']['event_type']
        event_des = mess_info['data']['event_description']
        min_in_game = mess_info['data']['min_in_game']
        date2 = date.datetime.now()
        date1 = date2.strftime('%Y-%m-%d')
        type_dict = {
            'Goal': EventTypeEnum.GOAL,
            'Yellow Card': EventTypeEnum.YELLOW_CARD,
            'Red Card': EventTypeEnum.RED_CARD
        }
        match_controller.add_event(game_id, referee_id, type_dict[event_type], event_des, date2, min_in_game, referee_id)
        return 'Success'
    except Exception as err:
        return str(err)

def edit_event(mess_info):
    try:
        referee_name = mess_info['data']['referee_id']
        referee = signed_user_controller.get_user_by_name(referee_name)
        referee_id = int(referee.user_id)
        game_id = int(mess_info['data']['game_id'])
        event_type = mess_info['data']['event_type']
        event_des = mess_info['data']['event_description']
        min_in_game = mess_info['data']['min_in_game']
        event_id = int(mess_info['data']['event_id'])
        date2 = date.datetime.now()
        type_dict = {
            'Goal': EventTypeEnum.GOAL,
            'Yellow Card': EventTypeEnum.YELLOW_CARD,
            'Red Card': EventTypeEnum.RED_CARD
        }
        match_controller.edit_event(event_id, type_dict[event_type], event_des, date2, min_in_game, referee_id, referee_id)
        return 'Success'
    except Exception as err:
        return str(err)


def get_all_users(mess_info):
    all_users = signed_user_controller.get_all_signed_users()
    all_users_final = []
    for user in all_users:
        mr_user = {
            'user_id': str(user.user_id),
            'user_name': user.user_name,
            'name': user.name,
            'birth_date': user.birth_date.strftime("%Y-%m-%d"),
            'role': str(type(user)).split('.')[1],
        }
        all_users_final.append(mr_user)
    return all_users_final


def get_all_refs(mess_info):
    all_refs = signed_user_controller.get_all_signed_users()
    all_refs_final = []
    for user in all_refs:
        if str(type(user)).split('.')[1] == 'Referee':
            mr_ref = {
                'User ID': str(user.user_id),
                'Username': user.user_name,
                'Qualification': str(user.qualification).split('.')[1],
                'Name': user.name,
                'Birth date': user.birth_date.strftime("%Y-%m-%d"),
            }
            all_refs_final.append(mr_ref)
    return all_refs_final

def get_all_teams(mess_info):
    all_teams = team_management_controller.get_all_teams()
    all_teams_final = []
    for team in all_teams:
        the_team = {
            'Team name': team.name,
            'Stadium': team.stadium,
            'Is open?': str(team.is_open),
        }
        all_teams_final.append(the_team)
    return all_teams_final

def get_all_game_events(mess_info):
    try:
        referee_name = mess_info['user_id']
        referee = signed_user_controller.get_user_by_name(referee_name)
        referee_id = int(referee.user_id)
        game_id = mess_info['data']['game_id']
        game_events_ids = match_controller.get_event_ids_from_game(game_id, referee_id)
        return game_events_ids
    except Exception as err:
        return str(err)

def delete_event(mess_info):
    try:
        referee_name = mess_info['user_id']
        referee = signed_user_controller.get_user_by_name(referee_name)
        referee_id = int(referee.user_id)
        event_id = int(mess_info['data']['event_id'])
        match_controller.remove_event(int(event_id), referee_id)
        return 'Success'
    except Exception as err:
        return str(err)


""" dictionary of all the handle functions - add your function to the dictionary """
handle_functions = {
    'get_user_info': get_user_info,
    'update_user_info': update_user_info,
    'user_login': user_login,
    'get_user_notifications': get_user_notifications,
    'user_register': user_register,
    'ref_register': ref_register,
    'remove_user': remove_user,
    'get_logs': get_logs,
    'add_policy': add_policy,
    'add_team': add_team,
    'get_users': get_all_users,
    'get_teams': get_all_teams,
    'get_refs': get_all_refs,
    'get_policy': get_policy,
    'get_on_going_games': get_on_going_games,
    'add_event': add_event,
    'edit_event': edit_event,
    'get_all_game_events': get_all_game_events,
    'delete_event': delete_event
}


def create_server(listen_port):
    return Server(listen_port, handle_message)


def error_mess():
    return 'Invalid Message Type'


def confirmation_massage():
    return 'Request Success'


def handle_message(message):
    message_info = json.loads(message)
    answer = handle_functions[message_info['type']](message_info)
    notifications = handle_functions['get_user_notifications'](message_info)
    ans_message = {
        'message': answer,
        'notifications': notifications
    }
    return json.dumps(ans_message)



server = create_server(10000)
server.listen()
