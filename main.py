list_fives = []
for i in range (1,101):
    if i % 5 == 0:
        list_fives.append(i)
print (list_fives)

list_power_of_three = [ z ** 3 for z in list_fives]
print (list_power_of_three)

for g in range (10):
    print(g)
    