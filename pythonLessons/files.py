# var = input('Напиши что-нибудь: ')
# fw = open('doc/file.txt', 'a')
# # fw.write('Hello world!\n') # вносим текст в файл
# fw.write(var)
# fw.close()

# "a" позволяет записывать ноавую информацию в конец списка в файле
# 'w' запись новых данных с удалением старых
# 'r' чтение


# fw = open('doc/file2.txt', 'w') # "a" позволяет записывать ноавую информацию в конец списка в файле
# fw.write('Privet') # вносим текст в файл
# fw.close()

# fr = open('doc/file.txt', 'r')
# text = fr.read()
# fr.close()
# print(text)

# r: Открывает файл в режиме только для чтения. Начинает чтение с начала файла и является режимом по умолчанию для open() функции.
# rb: Открывает файл как доступный только для чтения в двоичном формате и начинает чтение с начала файла. Хотя двоичный формат может использоваться для разных целей, он обычно используется при работе с такими вещами, как изображения, видео и т.д.
# r+: Открывает файл для чтения и записи, помещая указатель в начало файла.
# w: Открывается в режиме только для записи. Указатель помещается в начало файла, и это перезапишет любой существующий файл с тем же именем. Он создаст новый файл, если файл с таким же именем не существует.
# wb: Открывает файл, доступный только для записи, в двоичном режиме.
# w+: Открывает файл для записи и чтения.
# wb+: Открывает файл для записи и чтения в двоичном режиме.
# a: Открывает файл для добавления в него новой информации. Указатель размещается в конце файла. Новый файл создается, если файл с таким же именем не существует.
# ab: Открывает файл для добавления в двоичном режиме.
# a+: Открывает файл как для добавления, так и для чтения.
# ab+: Открывает файл как для добавления, так и для чтения в двоичном режиме.

# HW
# С текстом
with open('doc/hw.txt', 'w') as fw:
    fw.write('Beauty runs so deep')

with open('doc/hw.txt', 'a') as fa:
    fa.write("\nthat it's hard to sleep at night...")

with open('doc/hw.txt', 'r') as fr:
    text = fr.read()
    print(text)

with open('doc/hw.txt', 'r+') as frw:
    text = frw.read()
    frw.write("\nThis is the chapter of the forest...")
    print(text)

with open('doc/hw.txt', 'r') as fr:
    text = fr.read()
    print(text)


# С числами
with open('doc/hw_num.txt', 'w') as fw:
    print(23, file=fw)

with open('doc/hw_num.txt', 'r') as fr:
    new_num = int(input('Введите число: '))
    saved = int(fr.read())
    result = saved + new_num
    if result <= 50:
        print(saved + new_num)

with open('doc/hw_num.txt', 'a') as fa:
    first_num = int(input('Введите первое число: '))
    second_num = int(input('Введите второе число: '))
    result = first_num + second_num
    if result > 55:
        result += 1
    print(result, file=fa)

with open('doc/hw_num.txt', 'r+') as frw:
    text = frw.read()
    first_num = int(input('Введите число больше 10: ')) * 5
    second_num = int(input('Введите число меньше 20: ')) / 3
    result = int(first_num - second_num)
    if result > 70:
        result += 5
    print(result, file=frw)

with open('doc/hw_num.txt', 'r') as fr:
    text = fr.read()
    print(text)