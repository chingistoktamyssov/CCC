values = {'1': 100, '2': 500, '3': 1000, '4': 5000, '5': 10000, '6': 25000, '7': 50000, '8': 100000, '9': 500000, '10': 1000000}
total = 1691600

n = int(input())
for i in range(n):
  total -= values[input()]
  
offer = int(input())
if offer > total / (10 - n): print('deal')
else: print('no deal')