from WAStar import WeightedAStar
from pancake import PancakeNode
import random

random.seed(42)  # this makes sure that the random pattern repeats itself

wastar = WeightedAStar(w=1.05)
start = PancakeNode(pancakes=30, g=0, gap=0)

goal,expanded = wastar.search(start)

# backtrack solution
p = goal
solution = []
while p is not None:
    solution.append(p)
    p = p.pred
solution = solution[::-1]  # reverse

print(goal)
print('road to goal: ' + str(solution))
print('length of solution: ' + str(len(solution)))
print('number of expanded nodes: '+str(expanded))