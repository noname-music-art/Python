user_input = input()
len(user_input)
hours = 0
minutes = 0
for char in user_input:
    if char == '*':
        hours += 1
    elif char == ".":
        minutes += 15
    else:
        print("wrong element")
print(f"{hours}:{minutes}")