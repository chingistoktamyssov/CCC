books = input()

l = 0; m = 0

for i in books:
  if i == 'L':
    l += 1
  elif i == 'M':
    m += 1

lsec = books[:l]
msec = books[l:l+m]

m_in_l = 0
notl_in_l = 0

for i in lsec:
  if i == 'M':
    m_in_l += 1
  if i != 'L':
    notl_in_l += 1

l_in_m = 0
notm_in_m = 0

for i in msec:
  if i == 'L':
    l_in_m += 1
  if i != 'M':
    notm_in_m += 1

switches = notl_in_l + notm_in_m - min(l_in_m, m_in_l)

print(switches)