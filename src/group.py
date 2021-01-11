"""Holds the group class"""
import numpy as np

from enums import ChallengeType


class Group:
    """Represents a group of robots"""

    def __init__(self, teams: dict):
        # This is the dictionary created by a teams get_raw_score method
        self.teams = teams

    def _get_raw_bounds(self) -> dict:
        """Gets the raw bounds for each challenge"""
        raw_scores = []
        for team in self.teams:
            raw_scores.append(team.scores)
        bounds = {}
        for challenge in ChallengeType:
            challenge_scores = [team[challenge.name] for team in self.teams]
            q1, q3 = np.percentile(challenge_scores, 25), np.percentile(
                challenge_scores, 25
            )
            IQR = q3 - q1
            bounds[challenge.name]["lower"] = q1 - IQR
            bounds[challenge.name]["upper"] = q3 - IQR
        return bounds

    def _bind_scores(self) -> None:
        """Binds all of the team's raw_scores"""
        raw_bounds = self._get_raw_bounds()
        for team in self.teams:
            for team_challenge in team:
                bounds = raw_bounds[team_challenge]
                team[team_challenge]["bounded_score"] = max(
                    min(team_challenge["raw_score"], bounds["upper"]), bounds["lower"]
                )

    def calculate_rankings(self):
        pass
