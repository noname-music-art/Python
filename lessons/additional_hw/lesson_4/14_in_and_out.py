print("Available commands: stop, enter:object, exit:object")
data = []
enter_dict = {}
exit_dict = {}
while data != "stop":
    data = input()
    if data != "stop" and ("enter:" in data):
        data = data.split(":")
        enter_dict[data[1]] = data[0]
    elif data != "stop" and ("exit:" in data):
        data = data.split(":")
        exit_dict[data[1]] = data[0]

print(f"{enter_dict.keys()-exit_dict.keys()}")
print(f"{exit_dict.keys()-enter_dict.keys()}")
