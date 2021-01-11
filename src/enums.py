"""Holds some enums"""

import enum


class ChallengeType(enum.Enum):
    galactic_search = 0
    autonav = 1
    hyperdrive = 2
    interstellar_accuracy = 3
    power_port = 4


class TeamLevel(enum.Enum):
    beginner = 0
    intermediate = 1
    advanced = 2
