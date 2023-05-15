p1 = input()
p2 = input()

capital = 'ABCDE'

def genecheck(gene, p1, p2):
  if gene in capital:
    if gene in p1 or gene in p2:
      return True
  else:
    if gene in p1 and gene in p2:
      return True
  return False

for i in range(int(input())):
  possibility = True
  child = input()
  
  for j in child:
    if genecheck(j, p1, p2) == False:
      possibility = False
      print('Not their baby!')
      break
      
  if possibility == True:
    print('Possible baby.')