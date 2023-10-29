from enum import Enum


class KeyPointLabel(Enum):
    OPEN = 0
    CLOSE = 1
    POINTER = 2
    OK = 3
    PEACE = 4
    TEST = 5
    KOREAN_HEART = 6


class PointHistoryLabel(Enum):
    STOP = 0
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = 2
    MOVE = 3