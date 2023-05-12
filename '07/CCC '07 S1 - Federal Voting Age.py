for i in range(int(input())):
  birthday = input().split()
  year = int(birthday[0])
  month = int(birthday[1])
  day = int(birthday[2])

  if year < 1989:
    print('Yes')
  elif year == 1989:
    if month < 2:
      print('Yes')
    elif month == 2:
      if day <= 27:
        print('Yes')
      else:
        print('No')
    else:
      print('No')
  else:
    print('No')