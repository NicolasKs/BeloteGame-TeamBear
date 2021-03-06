from entities.team import Team
from file_writers.write_to_txt_helpers import format_team_names, format_output_for_first_and_last_rounds, \
    format_middle_round_output, \
    format_game_end_output


class WriteToTxt:

    def __init__(self, team1: Team, team2: Team):
        self.chars_before_vertical_separator = 0
        self.chars_after_vertical_separator = 0

        self.horizontal_separator_length = 0

        self.current_points_team1 = 0
        self.current_points_team2 = 0

        self.file = open('result.txt', 'w')

        self.__setting_up_txt_teams(team1, team2)

    def write_results(self, team1_points, team2_points, round_id):
        if round_id == 1:
            self.__write_first_round_results(team1_points, team2_points)
        else:
            self.__write_round_results(team1_points, team2_points)

    def write_game_end_output(self, team1, team2):

        self.__set_teams_current_points(team1.team_points, team2.team_points)

        self.file.write(
            format_output_for_first_and_last_rounds(self.current_points_team1, self.chars_before_vertical_separator,
                                                    self.current_points_team2, self.chars_after_vertical_separator))

        game_end_output = format_game_end_output(
            team1.games_won, self.chars_before_vertical_separator,
            team2.games_won, self.chars_after_vertical_separator,
            self.horizontal_separator_length)

        self.file.write(game_end_output)

    def __setting_up_txt_teams(self, team1, team2):
        team_names = f'    {team1.team_name}    |    {team2.team_name}    \n'
        self.__set_properties(team_names)
        self.file.write(format_team_names(team_names, self.horizontal_separator_length))

    def __set_properties(self, team_names):
        self.horizontal_separator_length = len(team_names) - 1
        self.chars_before_vertical_separator = team_names.index("|")
        self.chars_after_vertical_separator = len(team_names) - self.chars_before_vertical_separator - 1

    def __set_teams_current_points(self, team1_points, team2_points):
        self.current_points_team1 = team1_points
        self.current_points_team2 = team2_points

    def __write_to_file_and_set_attributes(self, output, team1_points, team2_points):
        self.file.write(output)
        self.__set_teams_current_points(team1_points, team2_points)

    def __write_first_round_results(self, team1_points, team2_points):
        output = format_output_for_first_and_last_rounds(
            team1_points, self.chars_before_vertical_separator,
            team2_points, self.chars_after_vertical_separator)

        self.__write_to_file_and_set_attributes(output, team1_points, team2_points)

    def __write_round_results(self, team1_points, team2_points):
        new_points_team1 = abs(self.current_points_team1 - team1_points)
        new_points_team2 = abs(self.current_points_team2 - team2_points)

        output = format_middle_round_output(
            self.current_points_team1, new_points_team1, self.chars_before_vertical_separator,
            self.current_points_team2, new_points_team2, self.chars_after_vertical_separator)

        self.__write_to_file_and_set_attributes(output, team1_points, team2_points)

    def __del__(self):
        self.file.close()


def main():
    pass


if __name__ == '__main__':
    main()
