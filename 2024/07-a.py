from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

def compute(nums, goal):
    nums = nums.split(" ")
    if len(nums) == 1:
        return goal == nums[0]

    n0 = int(nums[0])
    n1 = int(nums[1])
    suffix = nums[2:]

    if compute(" ".join([str(n0+n1)] + suffix), goal):
        return True

    if compute(" ".join([str(n0*n1)] + suffix), goal):
        return True

    return False

result = 0
for l in a:
    goal, nums = l.split(": ")

    if compute(nums, goal):
        result += int(goal)
    
print(result)

print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')