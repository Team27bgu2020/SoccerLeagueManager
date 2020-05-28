import json
from Server import Server
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from Service.PageController import PageController
from Service.TeamManagementController import TeamManagementController
from Service.UnionController import UnionController
from Service.NotificationsController import NotificationController

from DataBases.UserDB import UserDB
from DataBases.PolicyDB import PolicyDB
from DataBases.ComplaintDB import ComplaintDB
from DataBases.GameDB import GameDB
from DataBases.LeagueDB import LeagueDB
from DataBases.PageDB import PageDB
from DataBases.SeasonDB import SeasonDB
from DataBases.TeamDB import TeamDB

import datetime as date

""" This class is the controller that connects the server to the Domain """

signed_user_controller = SignedUserController(UserDB())
notification_controller = NotificationController()
signed_user_controller.add_fan_to_data('dor', '1234', 'dor', date.datetime(1994, 1, 20), '0.0.0.0')




def user_login(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    if not signed_user_controller.confirm_user(user_name, password):
        return 'Error'
    else:
        user = signed_user_controller.get_user(user_name)
        return {
                    'user_name': user_name,
                    'user_type': str(type(user)).split('.')[1],
                    'user_notification': notification_controller.check_user_notifications(user)
                }


def user_register(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    role = mess_info['data']['role']
    if signed_user_controller.get_user(user_name) is None:
        try:
            if role == 'Fan':
                signed_user_controller.add_fan_to_data(user_name, password, name,
                                                    date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
            elif role == "Team Owner":
                signed_user_controller.add_team_owner_to_data(user_name, password, name,
                                                          date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
            elif role == 'Union Representor':
                signed_user_controller.add_union_representor(user_name, password, name,
                                                        date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
            elif role == 'System Admin':
                signed_user_controller.add_system_admin(user_name, password, name,
                                                          date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
            else:
                return 'Error'
        except Exception:
            return 'Error'
        if str(type(signed_user_controller.get_user(user_name))).split('.')[1] == 'TeamUser':
            return {
                'user_name': user_name,
                'user_type': str(type(signed_user_controller.get_user(user_name).role)).split('.')[1]
            }
        else:
            return {
                'user_name': user_name,
                'user_type': str(type(signed_user_controller.get_user(user_name))).split('.')[1]
            }
    else:
        return 'Username Error'


def ref_register(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    qualification = mess_info['data']['qualification']
    if signed_user_controller.get_user(user_name) is None:
        try:
            signed_user_controller.add_referee_to_data(qualification, user_name, password, name,
                                                          date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
        except Exception:
            return 'Error'
    else:
        return 'Username Error'


def remove_user(mess_info):
    user_name = mess_info['data']['user_name']
    if signed_user_controller.get_user(user_name) is None:
            return 'Error'
    else:
        signed_user_controller.delete_signed_user(user_name)
        return 'Success'

def get_user_info(mess_info):
    """ Change implementation """
    return {
        'user name': 'Dor123',
        'first name': 'Dor',
        'last name': 'Pinhas'
    }


def update_user_info(mess_info):
    try:
        signed_user_controller.edit_personal_data(signed_user_controller.get_user(mess_info['user_id']),
                                mess_info['data']['user_name'], mess_info['data']['password'], mess_info['data']['name'],
                                date.datetime.strptime(mess_info['data']['birth_date'], '%Y-%m-%d'))
        return confirmation_massage()
    except Exception:
        return 'Error'


def get_user_notifications(mess_info):
    user_name = mess_info['data']['user_name']
    try:
        user = signed_user_controller.get_user(user_name)
        return {
                    'user_name': user_name,
                    'user_notifications': notification_controller.check_user_notifications(user)
            }
    except Exception as err:
        return err


""" dictionary of all the handle functions - add your function to the dictionary """
handle_functions = {
                    'get_user_info': get_user_info,
                    'update_user_info': update_user_info,
                    'user_login': user_login,
                    'get_user_notifications': get_user_notifications,
                    'user_register': user_register,
                    'ref_register': ref_register,
                    'remove_user': remove_user
}


def create_server(listen_port):
    return Server(listen_port, handle_message)


def error_mess():
    return 'Invalid Message Type'


def confirmation_massage():
    return 'Request Success'


def handle_message(message):
    message_info = json.loads(message)
    print(message_info)
    return json.dumps(handle_functions[message_info['type']](message_info))



server = create_server(10000)
server.listen()
