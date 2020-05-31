from Domain.TeamUser import TeamUser
from Domain.Player import Player
from Domain.Coach import Coach
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.UnionRepresentor import UnionRepresentor
from Domain.Referee import Referee
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Domain.Fan import Fan
from Domain.SystemAdmin import SystemAdmin

from datetime import date


def create_player(user_dict):

    player_role = Player(user_dict['assigned_by'], user_dict['position'], user_dict['number'])

    team_user = TeamUser(user_dict['user_name'], user_dict['password'], user_dict['name'],
                    get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['team'], player_role)

    team_user.notifications = user_dict['notifications']

    return team_user


def create_coach(user_dict):

    coach_role = Coach(user_dict['assigned_by'], user_dict['qualifications'])

    team_user = TeamUser(user_dict['user_name'], user_dict['password'], user_dict['name'],
                    get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['team'], coach_role)

    team_user.notifications = user_dict['notifications']

    return team_user


def create_team_manager(user_dict):

    team_manager_role = TeamManager(user_dict['assigned_by'], user_dict['open_close_permission'],
                                    user_dict['accounting_permission'], user_dict['add_remove_permission'],
                                    user_dict['set_permissions_permission'])

    team_user =  TeamUser(user_dict['user_name'], user_dict['password'], user_dict['name'],
                    get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['team'], team_manager_role)

    team_user.notifications = user_dict['notifications']

    return team_user


def create_team_owner(user_dict):

    additional_roles = []

    for role_doc in user_dict['additional_roles']:
        role = doc_to_role(role_doc)
        additional_roles.append(role)

    team_owner_role = TeamOwner(user_dict['assigned_by'], additional_roles)

    team_user =  TeamUser(user_dict['user_name'], user_dict['password'], user_dict['name'],
                    get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['team'], team_owner_role)

    team_user.notifications = user_dict['notifications']

    return team_user


def doc_to_role(role_doc):
    return role_dictionary[role_doc['role']](role_doc)


def create_union_representor(user_dict):

    user = UnionRepresentor(user_dict['user_name'], user_dict['password'], user_dict['name'],
                            get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['salary'])

    user.notifications = user_dict['notifications']

    return user

def create_referee(user_dict):

    qualifications = {'MAIN': RefereeQualificationEnum.MAIN, 'REGULAR': RefereeQualificationEnum.REGULAR}

    referee = Referee(qualifications[user_dict['qualification']], user_dict['user_name'], user_dict['password'],
                      user_dict['name'], get_birth_date_object(user_dict['birth_date']), user_dict['user_id'])
    referee.referee_in_games = user_dict['referee_in_games']
    referee.events = user_dict['events']
    referee.notifications = user_dict['notifications']

    return referee


def create_fan(user_dict):

    user =  Fan(user_dict['user_name'], user_dict['password'], user_dict['name'],
               get_birth_date_object(user_dict['birth_date']), user_dict['user_id'], user_dict['followed_pages'].copy(),
               user_dict['followed_games'].copy(), user_dict['complaints'].copy(), user_dict['recommendation_system'])

    user.notifications = user_dict['notifications']

    return user


def create_system_admin(user_dict):

    user = SystemAdmin(user_dict['user_name'], user_dict['password'], user_dict['name'],
                       get_birth_date_object(user_dict['birth_date']), user_dict['user_id'])

    user.notifications = user_dict['notifications']

    return user


def get_birth_date_object(birth_date_str: str):

    date_arr = birth_date_str.split('.')

    return date(int(date_arr[2]), int(date_arr[1]), int(date_arr[0]))


def doc_to_user(user_dict):

    return user_dictionary[user_dict['role']](user_dict)


def player_doc_to_role(role_doc):
    return Player(role_doc['assigned_by'], role_doc['position'], role_doc['number'])


def coach_doc_to_role(role_doc):
    return Coach(role_doc['assigned_by'], role_doc['qualification'])


def team_manager_doc_to_role(role_doc):
    return TeamManager(role_doc['assigned_by'], role_doc['open_close_permission'], role_doc['accounting_permission'],
                       role_doc['add_remove_permission'], role_doc['set_permissions_permission'])


role_dictionary = {
    'player': player_doc_to_role,
    'coach': coach_doc_to_role,
    'team_manager': team_manager_doc_to_role,
}


user_dictionary = {
    'player': create_player,
    'coach': create_coach,
    'team_manager': create_team_manager,
    'team_owner': create_team_owner,
    'union_representor': create_union_representor,
    'referee': create_referee,
    'fan': create_fan,
    'system_admin': create_system_admin
}
