"""Calculates the a robots average ranking in a group"""


from enums import TeamLevel, ChallengeType
from team import Team
from group import Group
from SkillChallenge import SkillChallenge
from random import randint, choice
import yaml


with open("src/team_constants.yml", "r") as team_file:
    team_info = yaml.load(team_file, Loader=yaml.Loader)


team_levels = [team_level for team_level in TeamLevel]
team_nums = set()
while len(team_nums) < 30:
    team_nums.add(randint(1, 9000))
team_list = []
for team in team_nums:
    team_level = choice(team_levels)
    team_challenges = []
    for challenge in ChallengeType:
        if challenge.name in team_info[team_level.name]:
            team_challenges.append(SkillChallenge(challenge))
    team_list.append(Team(team, team_level, team_challenges))
my_group = Group(team_list)
my_group._bind_scores()
print(my_group._get_challenge_computed_range())


# Take user input for what they want their robot to be
# Take number of beginner, intermediate, and advanced robots they want in group
# Form objects of the robots in the group
# Calculate computed score for each robot in the group
# Rank the robots
# Calculate and display percentages for each placement of the user robot, use pygal
