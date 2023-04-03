while True:
  factors = []
  dimensions = []
  n = int(input())
  if n == 0:
    break
  else:
    for x in range(1, n +1):
      if n % x == 0:
        factors.append(x)
    if len(factors) % 2 == 0:
      dimensions.append(factors[int(len(factors) / 2 - 1)])
      dimensions.append(factors[int(len(factors) / 2)])
    else:
      dimensions.append(factors[len(factors) // 2])
      dimensions.append(factors[len(factors) // 2])
    perimeter = dimensions[0] * 2 + dimensions[1] * 2
    print('Minimum perimeter is ' + str(perimeter) + ' with dimensions ' + str(dimensions[0]) + ' x ' + str(dimensions[1]))