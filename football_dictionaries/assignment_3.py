def players_by_country_and_position(squads_list):
    group_players_by_country_and_position_dict = {}

    for player in squads_list:
        country = player['country']
        position = player['position']

        if country not in group_players_by_country_and_position_dict:
            group_players_by_country_and_position_dict[country] = {}

        if position not in group_players_by_country_and_position_dict[country]:
            group_players_by_country_and_position_dict[country][position] = []

        group_players_by_country_and_position_dict[country][position].append(player)

    return group_players_by_country_and_position_dict
