from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
