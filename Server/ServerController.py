import json
from Server import Server


""" This class is the controller that connects the server to the Domain """


def get_user_info(mess_info):
    """ Change implementation """
    return {
        'user name': 'Dor123',
        'first name': 'Dor',
        'last name': 'Pinhas'
    }

def update_user_info(mess_info):
    """ Change implementation """
    print(mess_info)
    return confirmation_massage()


""" dictionary of all the handle functions - add your function to the dictionary """
handle_functions = {
                    'get_user_info': get_user_info,
                    'update_user_info': update_user_info
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