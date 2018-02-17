users = {'Alex': {'city': 'moscow', 'temperature': -10, 'wind': 12} , 
		'Ann': {'city': 'berlin', 'temperature': -5, 'wind': 3}, 
		'Omar': {'city': 'stambul', 'temperature': 15, 'wind': 7}}

name = input ('Введите имя')

print (users.get(name, 'Нет такого имени'))
name = input('Ваше имя: ')
b = input('Ваш город ')
с = input('temperature ' )
e = input('wind ')

users[name]={'city': b, 'temperature': c, 'wind': e}

users.sort()
print(users)
