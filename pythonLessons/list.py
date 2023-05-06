personal = ['Alex', 'Ivan', 'Natalia', 'Olga']

print(personal)

personal.append('Fedor')
print(personal)

# result = personal[0] + ' and ' + personal[2]
# # print(result + ' лучшая пара')
#
number = [23, 45, 67, 104]
# num_1 = number[1]
# num_3 = number[3]
# result_num = num_1 + num_3
# print(result_num)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(number) #выводми список
# print(number[:5]) # C 0 по 4
# print(number[5:]) # C 5 до конца
# print(number[5:10]) # C 5 до 9
# print(number[::5]) # Шаг 5
# print(number[1::3]) # C начиная с 1 и шагом 3
# print(number[:-4]) # Все кроме 4 последних
# print(number[1:-1]) # Без первого и последнего
# print(number[::-1]) # Реверс списка
# print(number[::-2]) # Реверс с шагом 2
# print(number[-2::-2]) #Реверс с 2 с конца и щагом 2
# print(number[10::-15])
#
# print(personal[1:]) # со второго объекта и до конца

pn = []

pn.append(personal) # добавляем список personal в новый список pn
pn.append(number) # добавляем список number в новый список pn

print(pn)
