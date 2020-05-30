def create_player(player, role):

    return {
        'user_id': player.user_id,
        'user_name': player.user_name,
        'password': player.password,
        'role': role,
        'name': player.name,
        'birth_date': str(player.birth_date.day) + '.' + str(player.birth_date.month) + '.' + str(player.birth_date.year),
        'notifications': player.notifications,
        'team': player.team,
        'assigned_by': player.role.assigned_by,
        'position': player.role.position,
        'number': player.role.number
    }


def create_coach(coach, role):

    return {
        'user_id': coach.user_id,
        'user_name': coach.user_name,
        'password': coach.password,
        'role': role,
        'name': coach.name,
        'birth_date': str(coach.birth_date.day) + '.' + str(coach.birth_date.month) + '.' + str(coach.birth_date.year),
        'notifications': coach.notifications,
        'team': coach.team,
        'assigned_by': coach.role.assigned_by,
        'qualifications': coach.role.qualification
    }


def create_team_manager(team_manager, role):

    return {
        'user_id': team_manager.user_id,
        'user_name': team_manager.user_name,
        'password': team_manager.password,
        'role': role,
        'name': team_manager.name,
        'birth_date': str(team_manager.birth_date.day) + '.' + str(team_manager.birth_date.month) + '.' + str(team_manager.birth_date.year),
        'notifications': team_manager.notifications,
        'team': team_manager.team,
        'assigned_by': team_manager.role.assigned_by,
        'open_close_permission': team_manager.role.approval_open_close,
        'accounting_permission': team_manager.role.approval_accounting,
        'add_remove_permission': team_manager.role.approval_add_remove,
        'set_permissions_permission': team_manager.role.approval_set_permission
    }


def create_team_owner(team_owner, role):
    role_list = []

    for owner_role in team_owner.role.roles:
        role_doc = role_to_doc(owner_role)
        role_list.append(role_doc)

    return {
        'user_id': team_owner.user_id,
        'user_name': team_owner.user_name,
        'password': team_owner.password,
        'role': role,
        'name': team_owner.name,
        'birth_date': str(team_owner.birth_date.day) + '.' + str(team_owner.birth_date.month) + '.' + str(team_owner.birth_date.year),
        'notifications': team_owner.notifications,
        'team': team_owner.team,
        'assigned_by': team_owner.role.assigned_by,
        'additional_roles': role_list
    }


def create_union_representor(union_rep, role):

    return {
        'user_id': union_rep.user_id,
        'user_name': union_rep.user_name,
        'password': union_rep.password,
        'role': role,
        'name': union_rep.name,
        'birth_date': str(union_rep.birth_date.day) + '.' + str(union_rep.birth_date.month) + '.' + str(union_rep.birth_date.year),
        'notifications': union_rep.notifications,
        'salary': union_rep.salary
    }


def create_referee(referee, role):

    return {
        'user_id': referee.user_id,
        'user_name': referee.user_name,
        'password': referee.password,
        'role': role,
        'name': referee.name,
        'birth_date': str(referee.birth_date.day) + '.' + str(referee.birth_date.month) + '.' + str(referee.birth_date.year),
        'notifications': referee.notifications,
        'qualification': str(referee.qualification).split('.')[1],
        'events': referee.events,
        'referee_in_games': referee.referee_in_games
    }


def create_fan(fan, role):

    return {
        'user_id': fan.user_id,
        'user_name': fan.user_name,
        'password': fan.password,
        'role': role,
        'name': fan.name,
        'birth_date': str(fan.birth_date.day) + '.' + str(fan.birth_date.month) + '.' + str(fan.birth_date.year),
        'notifications': fan.notifications,
        'followed_pages': fan.followed_pages,
        'followed_games': fan.followed_games,
        'complaints': fan.complaints,
        'recommendation_system': fan.recommendation_system
    }


def create_system_admin(system_admin, role):

    to_return = {
        'user_id': system_admin.user_id,
        'user_name': system_admin.user_name,
        'password': system_admin.password,
        'role': role,
        'name': system_admin.name,
        'birth_date': str(system_admin.birth_date.day) + '.' + str(system_admin.birth_date.month) + '.' + str(system_admin.birth_date.year),
        'notifications': system_admin.notifications
    }

    return to_return


def user_to_doc(user, role):

    return user_dictionary[role](user, role)


def role_to_doc(role):
    return role_dictionary[type(role).__name__](role)


def player_role_to_doc(player_role):
    return {
        'role': 'player',
        'assigned_by': player_role.assigned_by,
        'position': player_role.position,
        'number': player_role.number
    }


def coach_role_to_doc(coach_role):
    return {
        'role': 'coach',
        'assigned_by': coach_role.assigned_by,
        'qualification': coach_role.qualification
    }


def team_manager_to_doc(team_manager_role):
    return {
        'role': 'team_manager',
        'assigned_by': team_manager_role.assigned_by,
        'open_close_permission': team_manager_role.bool_open_close,
        'accounting permission': team_manager_role.bool_accounting,
        'add_remove_permission': team_manager_role.bool_add_remove,
        'set_permissions_permission': team_manager_role.bool_set_permissions
    }


role_dictionary = {
    'Player': player_role_to_doc,
    'Coach': coach_role_to_doc,
    'TeamManager': team_manager_to_doc,
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