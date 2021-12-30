list_fives = []
for i in range (1,101):
    if i % 5 == 0:
        list_fives.append(i)
print (list_fives)

list_power_of_three = [ z ** 3 for z in list_fives]
print (list_power_of_three)

for g in range (10):
    print(g)

for z in range (20):
    if z >= 8:
        print(z)
 
print("'Hiszpańska inkwizycja" to najlepszy skecz Monty Pythona")

movies = ["Rambo", "Alien", "Star Wars"]
for i in movies:
  print (i)
