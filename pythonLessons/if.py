# age = 23
# name = "Natalie"

# if age == 25 and name == 'Natalie':
#     print('Мне 25 лет и меня зовут Natalie')
# elif age > 25:
#     print('Мне больше 25 лет')
# else:
#     print('Мне меньше 25 лет')

# if age == 25 or name == 'Natalie':
#     print('Мне 25 лет и меня зовут Natalie')
# else:
#     print('Мне меньше 25 лет')

# if "l" in name == 'Natalie':
#     print('Мне 25 лет и меня зовут Natalie')
# else:
#     print('Меня не зовут Natalie')

#########

pin = 1234
print('Введите пожалуйста ваш пин-код')
user_pin = int(input())

if pin == user_pin:
    print('Какую сумму вы хотите снять?')
else:
    print('Ошибка! Введите корректный пин код, у вас осталось 2 попытки')
    user_pin = int(input())
    if pin == user_pin:
        print('Какую сумму вы хотите снять?')
    else:
        print('Ошибка! Введите корректный пин код, у вас осталась 1 попытка')
        user_pin = int(input())
        if pin == user_pin:
            print('Какую сумму вы хотите снять?')
        else:
            print('Ваша карта заблокирована, пожалуйста братитесь в банк')
