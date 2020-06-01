import json
import hashlib
from Server import Server
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from Service.PageController import PageController
from Service.TeamManagementController import TeamManagementController
from Service.UnionController import UnionController
from Service.NotificationsController import NotificationController

from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.PolicyDB import PolicyDB
from DataBases.ComplaintDB import ComplaintDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.LeagueDB import LeagueDB
from DataBases.PageDB import PageDB
from DataBases.SeasonDB import SeasonDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB

from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum

import datetime as date
import csv

""" This class is the controller that connects the server to the Domain """

users_db = MongoUserDB()
team_db = MongoTeamDB()
policy_db = PolicyDB()
signed_user_controller = SignedUserController(users_db)
notification_controller = NotificationController(users_db, MongoGameDB())
team_management_controller = TeamManagementController(team_db, users_db)
signed_user_controller.add_system_admin('dor', '1234', 'dor', date.datetime(1994, 1, 20))
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
        return {
                'user_name': user_name,
                'user_type': str(type(user.role)).split('.')[1]
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
        points_policy = PointsCalculationPolicy(points_win, points_draw, points_lose)
        try:
            policy_db.add(points_policy)
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
        game_policy = GameSchedulePolicy(int(game_against_each_team), games_per_week, games_policy_enum)
        try:
            policy_db.add(game_policy)
        except:
            return 'Error policy exists'
    elif policy_type == 'budget':
        min_budget = mess_info['data']['min_budget']
        budget_policy = TeamBudgetPolicy(min_budget)
        try:
            policy_db.add(budget_policy)
        except:
            return 'Error policy exists'


def add_team(mess_info):
    team_name = mess_info['data']['team_name']
    user = mess_info['user_id']
    try:
        team_management_controller.open_new_team(team_name, signed_user_controller.get_user_by_name(user).user_id)
    except:
        return 'Error'


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
