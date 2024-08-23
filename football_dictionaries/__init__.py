from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries
from assignment_2 import players_by_position
from assignment_3 import players_by_country_and_position

# Assignment 1
SQUADS_DATA_DICT = players_as_dictionaries(SQUADS_DATA)
print('***\tAssignment 1\t***\nPlayers as dictionaries:\n{}\n\n'.format(SQUADS_DATA_DICT))

# Assignment 2
players_by_position_dict = players_by_position(SQUADS_DATA_DICT)
print('***\tAssignment 2\t***\nPlayers by Position:\n{}\n\n'.format(players_by_position_dict))

# Assignment 3
players_by_country_and_position_dict = players_by_country_and_position(SQUADS_DATA_DICT)
print('***\tAssignment 3\t***\nPlayers by Country and Position:\n{}'.format(players_by_country_and_position_dict))
