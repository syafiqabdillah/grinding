# copy this template to create new file

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# where the FUN is
def fun(s, t):
  # quick check if length is not same, surely not anagram
  if len(s) != len(t):
    return False

  # for every c in s/t, make a dict where the char is the key and the occurence is the value
  maps = {}
  mapt = {}

  for c in s:
    if c in maps:
      maps[c] = maps[c] + 1
    else:
      maps[c] = 1

  for c in t:
    if c in mapt:
      mapt[c] = mapt[c] + 1
    else:
      mapt[c] = 1

  # quick check if len of unique key is not the same 
  if len(set(maps)) != len(set(mapt)):
    return False

  # if all else passed check if every val of maps equals every val of mapt 
  for k in maps:
    try:
      if maps[k] != mapt[k]:
        return False
    except:
      # it means there is key in maps that is not in mapt
      return False

  return True

# [(case, expected), ...]
tests = [
  (("anagram", "nagaram"), True),
  (("rat", "car"), False),
]

# testing
for test in tests:
  res = 'correct' if fun(test[0][0], test[0][1]) == test[1] else 'incorrect'
  print(f'{test[0]} {test[1]} {res}')