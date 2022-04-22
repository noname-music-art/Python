# Input date
year = input("year : ")
month = input("month : ")
day = input("day : ")

# Get list of numbers fron date
listA = year + month + day

# Convert list to string
strA = "".join(listA)

# Triple sum values from string
strA = str(sum(map(int, str(strA))))
strA = str(sum(map(int, str(strA))))
strA = str(sum(map(int, str(strA))))

# Print result
print(f'''Число вашего рождения: {strA}, готовлю прогноз...

Вы очень нуждаетесь в том, чтобы другие люди любили вас и восхищались вами. 
Вы довольно самокритичны. У вас есть много скрытых возможностей, 
которые вы так и не использовали себе во благо. 
Хотя у вас и есть некоторые личные слабости, вы, в общем, способны их нивелировать. 
Дисциплинированный и уверенный с виду, на самом деле, 
вы склонны волноваться и чувствовать неуверенность.

Вы – легковерный дурачок.
Нумерология – это лженаука.
Не верьте в ерунду, изучайте математику!''')
