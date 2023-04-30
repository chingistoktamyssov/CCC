peppers = {'Poblano': 1500, 'Mirasol': 6000, 'Serrano': 15500, 'Cayenne': 40000, 'Thai': 75000, 'Habanero': 125000}

heatlevel = 0
for i in range(int(input())):
  heatlevel = heatlevel + peppers[input()]
  
print(heatlevel)