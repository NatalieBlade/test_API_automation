# глобальные и локальные переменные

var_1 = 100 #глобальная переменная - читается во всем коде
var_2 = 20 #глобальная переменная


def sum():
    # var_1 = 40 #локальная переменная - видит только функция
    # var_2 = 2 #локальная переменная
    result = var_1 + var_2
    print(result)
# print(var_1, var_2)

def sub():
    var_2 = 50
    result = var_1 - var_2
    print(result)

def umn():
    var_2 = 50
    result = var_1 * var_2
    print(result)

def devis():
    var_2 = 50
    result = var_1 / var_2
    print(int(result))

sum()
sub()
umn()
devis()
