def solve(cards):
  maxval = 0
  
  if len(cards) == 1:
    if cards[0] <= 24:
      return cards[0]
    return 0
    
  else:
    for i in range(len(cards)):
      for j in range(len(cards)):
        
        add1 = cards.copy()
        x = add1.pop(i)
        y = add1.pop(j-1)
        add1.append(x+y)
        add2 = solve(add1)

        sub1 = cards.copy()
        x = sub1.pop(i)
        y = sub1.pop(j-1)
        sub1.append(x-y)
        sub2 = solve(sub1)

        mult1 = cards.copy()
        x = mult1.pop(i)
        y = mult1.pop(j-1)
        mult1.append(x*y)
        mult2 = solve(mult1)

        div2 = 0
        div1 = cards.copy()
        x = div1.pop(i)
        y = div1.pop(j-1)
        if y != 0 and x % y == 0:
          div1.append(x//y)
          div2 = solve(div1)

        maxval = max(maxval, add2, sub2, mult2, div2)

    return maxval

for i in range(int(input())):
  cards = []
  for j in range(4):
    cards.append(int(input()))
  print(solve(cards))