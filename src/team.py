"""Holds the team class"""
from enums import TeamLevel


class Team:
    """Represents one team in a group"""

    def __init__(self, team_number: int, team_level: TeamLevel, team_challenges: list):
        self.team_number = team_number
        # Skill level of this team
        self.team_level = team_level
        # A list of the challenges they attempt, should be a ChallengeType obj
        self.team_challenges = team_challenges
        score_dict = {"team_number": self.team_number}
        for challenge in self.team_challenges:
            # For some reason you cannot assign subdicts that do not exist yet
            score_dict[challenge.challenge.name] = {}
            score_dict[challenge.challenge.name][
                "raw_score"
            ] = challenge.calculate_raw_score(self.team_level)
        # Represents the raw scores
        self.scores = score_dict

    def set_raw_scores(self, scores: dict):
        """Sets the scores, for the user defined team / teams"""
        self.scores = scores
