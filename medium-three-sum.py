# copy this template to create new file

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# where the FUN is
def fun(s):
  return []

# [(case, expected), ...]
tests = [
  ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
  ([0,1,1], []),
  ([0,0,0], [[0,0,0]])
]

# testing
for test in tests:
  res = 'correct' if fun(test[0]) == test[1] else 'incorrect'
  print(f'{test[0]} {test[1]} {res}')