"""Calculates the a robots average ranking in a group"""

import random

import numpy as np
import yaml

import SkillChallenge

# Constants

computed_max_score = 150


# Functions:
# Group min/max comp score
def get_group_range(num_challenge_participants: int):
    return (
        max(computed_max_score - 20 * (num_challenge_participants - 1), 50),
        computed_max_score,
    )


# Take user input for what they want their robot to be
# Take number of beginner, intermediate, and advanced robots they want in group
# Form objects of the robots in the group
# Calculate computed score for each robot in the group
# Rank the robots
# Calculate and display percentages for each placement of the user robot, use pygal
