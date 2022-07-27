# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def fun(nums) -> bool:
  return len(nums) != len(set(nums))

tests = [
  ([1,2,3,1], True),
  ([1,2,3,4], False),
  ([1,1,1,3,3,4,3,2,4,2], True),
]

for test in tests:
  res = 'correct' if fun(test[0]) == test[1] else 'incorrect'
  print(f'{test[0]} {res}')