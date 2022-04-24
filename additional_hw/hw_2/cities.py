cities = "архангельск - киров - вологда - адлер - рим - минск - киров"
cities = cities.replace(" - ", " ")
cities = cities.split(" ")

flag = False
last_char = None
first = True

for city in cities:
    if cities.count(city) > 1:
        flag = True

    if (last_char != city[0]) and not first:
        flag = True

    print(city[0], last_char)
    last_char = city[-1]
    first = False

if flag:
    print(f"Правила нарушены")
else:
    print(f"Правила не нарушены")