"""Holds the group class"""
import numpy as np

from enums import ChallengeType
from team import Team


class Group:
    """Represents a group of robots"""

    def __init__(self, teams: Team):
        # This is the dictionary created by a teams get_raw_score method
        self.teams = teams

    def _get_challenge_raw_scores(self) -> dict:
        """Gets the challenge scores for all teams in the group"""
        raw_scores = []
        for team in self.teams:
            raw_scores.append(team.scores)
        challenge_raw_scores = {
            "galactic_search": [],
            "autonav": [],
            "hyperdrive": [],
            "interstellar_accuracy": [],
            "power_port": [],
        }
        for team in raw_scores:
            for challenge in team:
                if challenge == "team_number":
                    continue
                challenge_raw_scores[challenge].append(team[challenge]["raw_score"])
        return challenge_raw_scores

    def _get_raw_bounds(self) -> dict:
        """Gets the raw bounds for each challenge"""
        bounds = {}
        challenge_raw_scores = self._get_challenge_raw_scores()
        for challenge in ChallengeType:
            q1 = np.percentile(challenge_raw_scores[challenge.name], 25)
            q3 = np.percentile(challenge_raw_scores[challenge.name], 75)
            IQR = q3 - q1
            bounds[challenge.name] = {}
            bounds[challenge.name]["lower"] = q1 - IQR
            bounds[challenge.name]["upper"] = q3 - IQR
        return bounds

    def _bind_scores(self) -> None:
        """Binds all of the team's raw_scores"""
        raw_bounds = self._get_raw_bounds()
        for team in self.teams:
            for team_challenge in team.team_challenges:
                bounds = raw_bounds[team_challenge.challenge.name]
                team.scores[team_challenge.challenge.name]["bounded_score"] = max(
                    min(
                        team.scores[team_challenge.challenge.name]["raw_score"],
                        bounds["upper"],
                    ),
                    bounds["lower"],
                )

    def _get_challenge_computed_range(self) -> dict:
        challenge_raw_scores = self._get_challenge_raw_scores()
        computed_max_score = 150
        range_dict = {}
        for challenge in challenge_raw_scores:
            range_dict[challenge] = {}
            range_dict[challenge]["computed_range"] = (
                max(computed_max_score - 20 * (len(challenge_raw_scores[challenge]) - 1), 50),
                computed_max_score,
            )
        return range_dict

    def calculate_rankings(self):
        pass
