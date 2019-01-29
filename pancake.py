import numpy as np
import random


class PancakeNode:
    # need to support expand(),calc_h(),is_goal()
    def __init__(self, pancakes, g=0, gap=0, pred=None):
        """
        Constructor of the pancake problem node
        :param pancakes: If int - number of random pancakes to generate (for initial node) if array - the pancakes array of the node
        :param g: Distance from initial node
        :param gap: gap for GAP-X heuristic function
        :param pred: pointer to the predecessor
        """
        if type(pancakes) is int:
            self.pancakes = list(range(1, pancakes + 1))
            random.shuffle(self.pancakes)
            self.plate = pancakes + 1
        else:  # pancakes is array
            self.pancakes = pancakes
            self.plate = max(pancakes) + 1
        self.g = g
        self.gap = gap
        self.pred = pred

    def __eq__(self, other):
        return self.pancakes == other.pancakes

    def __hash__(self):
        return hash(str(self.pancakes))

    def __repr__(self):
        return str(self.pancakes)

    def is_goal(self):
        return all(self.pancakes[i] <= self.pancakes[i + 1] for i in range(len(self.pancakes) - 1))

    def expand(self):
        """
        Expands the current node
        :return: List of all neighbouring nodes.
        """
        frontier = []
        for i in range(2, len(self.pancakes)):
            flipped = list(list(np.flip(self.pancakes[:i], axis=0)) + self.pancakes[i:])
            frontier.append(PancakeNode(flipped, self.g + 1, self.gap, self))
        flipped = list(np.flip(self.pancakes, axis=0))
        frontier.append(PancakeNode(flipped, self.g + 1, self.gap, self))
        return frontier

    def calc_h(self):
        """
        Calculate the heuristic of the current node according to the GAP-X function.
        :return: Heuristic according to the GAP-X function and the gap field.
        """
        count = 0
        for i in range(len(self.pancakes)):
            if i == len(self.pancakes) - 1:
                if self.pancakes[i] > self.gap and abs(self.pancakes[i] - self.plate) > 1:
                    count += 1
                continue
            if self.pancakes[i] <= self.gap or self.pancakes[i + 1] <= self.gap:
                continue
            if abs(self.pancakes[i] - self.pancakes[i + 1]) > 1:
                count += 1
        return count
