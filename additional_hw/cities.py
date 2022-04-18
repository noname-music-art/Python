cities = input()
cities = cities.replace(" - ", " ")
cities = cities.split(" ")

flag = False

for city in cities:
    if cities.count(city) > 1:
        flag = True
    print(city[0])
print(flag)
