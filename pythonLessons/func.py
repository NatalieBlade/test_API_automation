# num_1 = 5
# num_2 = 10
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 4
# result = num_1 + num_2
# print(result)

# num_1 = 30
# num_2 = 4
# def sum(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
# sum(num_2='world', num_1='Hello ') #Запуск функции

# name = 'Alex'
name = input()
age = input()
def hi(name, age):
    result = name + " " + age
    # print('My name is ' + name + ', мне ' + age + ' лет')
    # print(result)
    return result
# hi('Ivan')
# hi(name='Ivan')
h = hi(name, age)
print(h)

