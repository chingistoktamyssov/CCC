operators = '+ -'

while True:
  exp = input()
  if exp == "0":
    break 

  exp = exp.split()[::-1]

  stack = []
  for i in exp:
    if i in operators:
      a = stack.pop()
      b = stack.pop()
      stack.append(a + b + i)
          
    else:
      stack.append(i)
   
  print(" ".join(list(stack[0])))