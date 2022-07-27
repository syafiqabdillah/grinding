# copy this template to create new file

# description

# where the FUN is
def fun(arg):
  return True

# [(case, expected), ...]
tests = [
  ([1,2,3], True),
]

# testing
for test in tests:
  res = 'correct' if fun(test[0]) == test[1] else 'incorrect'
  print(f'{test[0]} {test[1]} {res}')