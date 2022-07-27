# copy this template to create new file

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# where the FUN is
def fun(nums, target):
  # naive: check all pairs - slowest
  # less naive: check all less than target - slow
  # for i in range(0, len(nums) - 1):
  #   for j in range(i + 1, len(nums)):
  #     sum = nums[i] + nums[j]
  #     if sum == target:
  #       return [i, j]

  mappast = {} # number as key, index as value

  for i in range(0, len(nums)):
    # check the diff 
    diff = target - nums[i] 
    # if diff in mappast -> is means found the target, return 
    if diff in mappast:
      return [mappast[diff], i]
    # else add nums[i] as key and i as value to mappast
    else:
      mappast[nums[i]] = i
  return [0, 0]

# [(case, expected), ...]
tests = [
  (([2,7,11,15], 9), [0,1]),
  (([3,2,4], 6), [1, 2]),
  (([3,3], 6), [0, 1]),
]

# testing
for test in tests:
  res = 'correct' if fun(test[0][0], test[0][1]) == test[1] else 'incorrect'
  print(f'{test[0]} {res}')