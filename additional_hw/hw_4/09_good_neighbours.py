elements = {28: "Никель", 29: "Медь", 30: "Цинк"}

chosen_element = int(input())

if chosen_element in elements.keys():
    print(f"{chosen_element} это {elements[chosen_element].lower()}", end="\nСоседи: \n")
if chosen_element-1 in elements.keys():
    print(chosen_element-1, elements[chosen_element-1])
if chosen_element+1 in elements.keys():
    print(chosen_element+1, elements[chosen_element+1])
