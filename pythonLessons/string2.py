# str_1 = 'hello'
# print(str_1)
# print(dir(str_1)) - все возможные действия с переменной
# str_2 = 'WORLD'
# print(str_2.lower())
# print(str_1.upper())
# print(str_1.title())


# name = 'Ivan'
# name = 'Alex'
# a = 'Hello {}' # {} означают, что туда можно поставить какое-либо значение
# result = a.format(name) #добавляем в {} имя
# print(result)

first_name = 'Ivan'
last_name = 'Ivanov'
a = '{} {}'
result = a.format(first_name, last_name)
print("My name is " + result)

result = f'{first_name} {last_name}'
print("My name is " + result)
