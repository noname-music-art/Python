test_layout = ("X_X_XX___XXX___XXXX")
test_layout = test_layout.split("_")

intruders = 0

for group in test_layout:
    if "X" in group and len(group) > 1:
        intruders += len(group)

print(intruders)
