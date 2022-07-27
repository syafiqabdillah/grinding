# copy this template to create new file

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# where the FUN is
def alphanum(c):
  return (
    ord("A") <= ord(c) <= ord("Z")
    or ord("a") <= ord(c) <= ord("z")
    or ord("0") <= ord(c) <= ord("9")
  )

def fun(s):
  left, right = 0, len(s) - 1
  while left < right:
    while left < right and not alphanum(s[left]):
      left += 1
    while left < right and not alphanum(s[right]):
      right -= 1
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

# [(case, expected), ...]
tests = [
  ("A man, a plan, a canal: Panama", True),
  ("race a car", False),
  (" ", True),
  ("0P", False),
]

# testing
for test in tests:
  res = 'correct' if fun(test[0]) == test[1] else 'incorrect'
  print(f'{test[0]} {test[1]} {res}')