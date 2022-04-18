user_input = input()

hours = 0
minutes = 0

for char in user_input:
    if char == '*':
        hours += 1
    elif char == ".":
        minutes += 15

hours = hours + minutes // 60
minutes = minutes % 60

print(f"{hours}:{minutes}")
