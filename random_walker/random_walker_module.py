import random
import math


class RandomWalker:
    """This class represent a random walker.
    It envolves x_pos as x position and y_pos as y position.
    The initial postion is (0, 0),
    and it makes some random steps using the step method.
    """

    def __init__(self):
        # This function is to initiate the attributes
        self.x_pos = 0
        self.y_pos = 0

    def step(self):
        # This function is to implement one step for random walker
        e_x = random.gauss(0, 1)
        e_y = random.gauss(0, 1)
        self.x_pos += e_x
        self.y_pos += e_y

    def get_x_pos(self):
        # This function is to get the x position of random walker
        return self.x_pos

    def get_y_pos(self):
        # This function is to get the y position of random walker
        return self.y_pos


class ModifiedRandomWalker(RandomWalker):
    """This class represent a modified random walker.
    It envolves x_pos as x position and y_pos as y position.
    The initial postion is (0, 0), and it makes some random steps
    with minimum distances among certain list using the step method."""

    def step(self, r0=RandomWalker(), r1=RandomWalker(), r2=RandomWalker()):
        # This is to overwrite a new step method

        # Create a list to represent the square distances between
        # the modified random walker and three other random walkers.
        dist = []

        x_dist = math.pow((r0.x_pos-self.x_pos), 2)
        y_dist = math.pow((r0.y_pos-self.y_pos), 2)
        dist.append(x_dist + y_dist)

        x_dist = math.pow((r1.x_pos-self.x_pos), 2)
        y_dist = math.pow((r1.y_pos-self.y_pos), 2)
        dist.append(x_dist + y_dist)

        x_dist = math.pow((r2.x_pos-self.x_pos), 2)
        y_dist = math.pow((r2.y_pos-self.y_pos), 2)
        dist.append(x_dist + y_dist)

        # Find which random walker is the closest to the modified random walker
        min_index = dist.index(min(dist))
        self.x_pos = [r0, r1, r2][min_index].x_pos
        self.y_pos = [r0, r1, r2][min_index].y_pos
