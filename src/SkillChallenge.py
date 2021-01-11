import random

import yaml

from enums import ChallengeType, TeamLevel

with open("challenges.yml", "r") as challenge_file:
    challenges = yaml.load(challenge_file, Loader=yaml.Loader)


class SkillChallenge:
    """Represents a challenge of a team"""

    def __init__(self, challenge: ChallengeType):
        self.challenge = challenge

    def calculate_raw_score(self, team_level: TeamLevel) -> tuple:
        """Calculates the raw score for this challenge of a team's skil level"""
        # Gets the skill levels predicted range
        predicted_range = challenges[self.challenge.name]["predicted_points"][
            team_level.name
        ]
        # If its a timed score, it can be a float, use random.uniform instead of random.randint
        if challenges[self.challenge.name]["is_timed_score"]:
            return round(
                random.uniform(predicted_range["min"], predicted_range["max"]), 2
            )
        else:
            return random.randint(predicted_range["min"], predicted_range["max"])
