burger = int(input())
side= int(input())
drink= int(input())
dessert = int(input())

burgerlist = [461, 431, 420, 0]
sidelist = [100, 57, 70, 0]
drinklist = [130, 160, 118, 0]
dessertlist = [167, 266, 75, 0]

total = burgerlist[burger - 1] + drinklist[drink - 1] + sidelist[side - 1] + dessertlist[dessert - 1]

print("Your total Calorie count is", str(total) + ".")