import math

numerator = int(input())
denominator = int(input())

simplify = math.gcd(numerator, denominator)

numerator = int(numerator / simplify)
denominator = int(denominator / simplify)

if denominator == 1:
  print(numerator)
else:
  if numerator // denominator == 0:
    print(str(numerator - numerator // denominator * denominator) + '/' + str(denominator))
  else:
    print(numerator // denominator, str(numerator - numerator // denominator * denominator) + '/' + str(denominator))