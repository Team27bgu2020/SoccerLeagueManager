import json
from Server import Server
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from Service.PageController import PageController
from Service.TeamManagementController import TeamManagementController
from Service.UnionController import UnionController

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
signed_user_controller.add_fan_to_data('dor', '1234', 'dor', date.datetime(1994, 1, 20), '0.0.0.0')


# signed_user_controller.add_system_admin('idan', '1234', 'idan', date.datetime(1994, 1, 20), '0.0.0.0')


def user_login(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    if not signed_user_controller.confirm_user(user_name, password):
        return 'Error'
    else:
        return {
            'user_name': user_name,
            'user_type': str(type(signed_user_controller.get_user(user_name))).split('.')[1]
        }


def user_register(mess_info):
    user_name = mess_info['data']['user_name']
    password = mess_info['data']['password']
    name = mess_info['data']['name']
    birth_date = mess_info['data']['birth_date']
    if signed_user_controller.get_user(user_name) is None:
        try:
            signed_user_controller.add_fan_to_data(user_name, password, name,
                                                   date.datetime.strptime(birth_date, '%Y-%m-%d'), '0.0.0.0')
        except Exception:
            return 'Error'
        return {
            'user_name': user_name,
            'user_type': str(type(signed_user_controller.get_user(user_name))).split('.')[1]
        }
    else:
        return 'Error'


def guest_login(mess_info):
    signed_user_controller.add_guest('0.0.0.0')
    return {
        'user_name': 'Guest',
        'user_type': 'Guest'
    }


def get_user_info(mess_info):
    """ Change implementation """
    return {
        'user name': 'Dor123',
        'first name': 'Dor',
        'last name': 'Pinhas'
    }


def update_user_info(mess_info):
    """ Change implementation """
    return confirmation_massage()


""" dictionary of all the handle functions - add your function to the dictionary """
handle_functions = {
    'get_user_info': get_user_info,
    'update_user_info': update_user_info,
    'user_login': user_login,
    'user_register': user_register,
    'guest_login': guest_login
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
