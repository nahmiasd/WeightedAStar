from sortedcontainers import SortedList


class WeightedAStar:

    def __init__(self, w):
        """
        Constructor of the WA* algorithm instance
        :param w: W of the WA* f(n)
        """
        self.w = w
        self.open = SortedList(key=lambda x: x.g + self.w * x.calc_h())  # priority queue based on f(n)
        self.closed = set()

    def restart(self):
        """
        Restarts the open and closed lists.
        :return:
        """
        self.open.clear()
        self.closed.clear()

    def search(self, start_node):
        """
        Searches from the start node provided.
        :param start_node: Initial state of the search space.
         Node should support the following interface: expand(),calc_h() and is_goal()
        :return: The goal node and the number of nodes expanded.
        """
        self.restart()
        expanded=0
        self.open.add(start_node)
        while len(self.open) != 0:
            node = self.open.pop(0)
            if node.is_goal():
                return node,expanded
            frontier = node.expand()
            expanded+=1
            for neighbour in frontier:
                if neighbour not in self.closed:
                    self.open.add(neighbour)
            self.closed.add(node)
