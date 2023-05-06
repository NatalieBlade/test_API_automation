# first_num = float(input('Введите первое значение: '))
# second_num = float(input('Введите второе значение: '))
# action = input('Введите арифметический знак, например: +,-,*,/')
# try:
#     first_num = int(input('Введите первое значение: '))
#     second_num = int(input('Введите второе значение: '))
#     action = input('Введите арифметический знак, например: +,-,*,/')
# except ValueError:
#     result = 0
#     print('Это не число. Введите число корректно')




# try:
#     # if first_num is not float or second_num is not float:
#     first_num = float(input('Введите первое значение: '))
#     second_num = float(input('Введите второе значение: '))
# except ValueError:
#     print('Это не число. Введите число корректно')
# try:
#     # if first_num is not float or second_num is not float:
#     action = input('Введите арифметический знак, например: +,-,*,/')
# except ValueError:
#     print('Некорректный арифметический знак')
# try:
#     # first_num = float(input('Введите первое значение: '))
#     # second_num = float(input('Введите второе значение: '))
#     # action = input('Введите арифметический знак, например: +,-,*,/')
#     if action == '+':
#         result = float(first_num + second_num)
#     elif action == '-':
#         result = float(first_num - second_num)
#     elif action == '*':
#         result = float(first_num * second_num)
#     elif action == '/':
#         result = float(first_num / second_num)
#     # else:
#     #     result = 0
#     #     print('Некорректный арифметический знак')
#
# except ZeroDivisionError:
#     result = 0
#     print('На ноль делить нельзя')
# # except ValueError:
# #     result = 0
# #     print('Это не число. Введите число корректно')
# if result == 0:
#     print("Результат " + str(result))
# elif int(str(result).split('.')[1]) > 0:
#     print("Результат " + str(result))
# else:
#     print("Результат " + str(result).split('.')[0])




# try:
#     # if first_num is not float or second_num is not float:
#     first_num = float(input('Введите первое значение: '))
#     second_num = float(input('Введите второе значение: '))
# except ValueError:
#     print('Это не число. Введите число корректно')
# try:
#     # if first_num is not float or second_num is not float:
#     action = input('Введите арифметический знак, например: +,-,*,/')
# except ValueError:
#     print('Некорректный арифметический знак')
try:
    first_num = float(input('Введите первое значение: '))
    action = input('Введите арифметический знак, например: +,-,*,/')
    second_num = float(input('Введите второе значение: '))
    if action == '+':
        result = float(first_num + second_num)
    elif action == '-':
        result = float(first_num - second_num)
    elif action == '*':
        result = float(first_num * second_num)
    elif action == '/':
        result = float(first_num / second_num)
    else:
        result = 0
        print('Некорректный арифметический знак. Пожалуйста повторите попытку')
except ValueError:
    result = 0
    print('Введено некорректное значение. Пожалуйста повторите попытку')
except ZeroDivisionError:
    result = 0
    print('На ноль делить нельзя!')

print("Результат " + str(result))
# if result == 0:
#     print("Результат " + str(result))
# elif float(str(result).split('.')[1]) >= 0:
#     print("Результат " + str(result))
# else:
#     print("Результат " + str(result).split('.')[0])

# if result is int:
#     print("Результат " + str(result))
# elif result is float:
#     if float(str(result).split('.')[1]) >= 0:
#         print("Результат " + str(result))
#     else:
#         print("Результат " + str(result).split('.')[0])

# else:
#     print("Результат " + str(result).split('.')[0])

# if int(str(result).split('.')[1]) > 0:
#     print("Результат " + str(result))
# else:
#     print("Результат " + str(result).split('.')[0])

# if float(str(result).split('.')[1]) >= 0:
#     print("Результат " + str(result))
# elif result == 0:
#     print("Результат " + str(result))
# else:
#     print("Результат " + str(result).split('.')[0])
