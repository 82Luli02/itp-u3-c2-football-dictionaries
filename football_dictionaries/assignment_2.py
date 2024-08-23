def players_by_position(squads_list):
  group_players_by_position_dict={}
    
  for player in squads_list:
    position = player['position']

    if position not in group_players_by_position_dict:
      group_players_by_position_dict[position]=[]

    group_players_by_position_dict[position].append(player)

  return group_players_by_position_dict
