# список
family_1 = ['Anna', 'Alex', 'Anton', 'Maria', 'Sergey', 'Alina', 'Anna']

print(family_1)

# множество - выдается в рандомном порядке, не выводит дубликаты, чувствительна к регистру
family_2 = {'Anna', 'Alex', 'Anton', 'Maria', 'Sergey', 'Alina'}
print(family_2)

# словарь - ключ:значение
family_3 = {'Папа':'Alex', 'Мама':'Anna', 'Дочь':'Alina', 'Сын':'Sergey'}
# print(famity_3['Сын'])
for k, v in family_3.items():
    print(k + ' - ' + v)