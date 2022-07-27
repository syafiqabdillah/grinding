# copy this template to create new file

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# where the FUN is
def fun(s):
  res = 0
  left = 0
  
  for right in range(1, len(prices)):
    if prices[right] < prices[left]: # rugi, pindahin min
      left = right
    res = max(res, prices[right] - prices[left])
  
  return res

# [(case, expected), ...]
tests = [
  
]

# testing
for test in tests:
  res = 'correct' if fun(test[0]) == test[1] else 'incorrect'
  print(f'{test[0]} {test[1]} {res}')