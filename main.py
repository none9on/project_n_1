def encryption(str1, code1, n):
    if n == 2:
        code1 = code1[::-1]
    code1 = list(map(int, code1))
    lengthstr = len(str1)
    lengthc = len(code1)
    if n == 1:
        str1 = str1.ljust(lengthstr + (lengthc - lengthstr % lengthc) % lengthc, "\0")
        lengthstr = len(str1)
    count = int(lengthstr / lengthc)
    a1 = 0
    a2 = lengthc
    str2 = ''
    for i in range(count):
        helpstr = str1[a1:a2]
        for j in code1:
            str2 += str(helpstr[j])
        a1 = a2
        a2 = a2 + lengthc
    if n == 2:
        while str2[-1] == ' ':
            str2 = str2[:-1]
    return str2


def encryption1(str1, code1, n):
    if n == 2:
        code1 = code1[::-1]
    code1 = list(map(int, code1))
    lengthc = len(code1)
    if n == 1:
        str1 = str1.split()
        lenstr = len(str1)
        while len(str1) != lenstr + (lengthc - lenstr % lengthc) % lengthc:
            str1.append('\0')
    elif n == 2:
        str1 = list(str1.replace(' ', ' \0 ').split(' '))
    lenstr = len(str1)
    count = int(lenstr / lengthc)
    a1 = 0
    a2 = lengthc
    string_2 = []
    for i in range(count):
        helpstr = str1[a1:a2]
        for j in code1:
            string_2.append(str(helpstr[j]))
        a1 = a2
        a2 = a2 + lengthc
    str3 = ''
    if n == 1:
        for i in string_2:
            str3 += i
    elif n == 2:
        for i in string_2:
            str3 += i + ' '
        str3 = str3.replace(' \0', '')
        str3 = str3[:-1]
    return str3


def encryption3(str1, code1, n, length1):
    if n == 2:
        code1 = code1[::-1]
    code1 = list(map(int, code1))
    lengthc = len(code1)
    lengthstr = len(str1)
    count_symbols = (length1 - lengthstr % length1) % length1
    str1 += '\0' * count_symbols
    lengthstr = len(str1)
    block = ''
    temporary = length1
    str2 = []
    for i in range(lengthstr):
        if temporary == 0:
            str2.append(block)
            block = ''
            temporary = length1
        block += str1[i]
        temporary -= 1
    str2.append(block)
    lengthstr = len(str2)
    count = int(lengthstr / lengthc)
    a1 = 0
    a2 = lengthc
    str3 = ''
    for i in range(count):
        helpstr = str2[a1:a2]
        for j in code1:
            str3 += str(helpstr[j])
        a1 = a2
        a2 = a2 + lengthc
    if n == 2:
        while str3[-1] == ' ':
            str3 = str3[:-1]
    return str3

print('Добро пожаловать в приложение для шифрования и дешифровки текста - "ENCRY".')
while True:
    print('Для зашифрования текста введите "1"\nДля дешифровки введите -"2"\nДля выхода из приложения - "0"')
    num = input()
    num = int(num)
    if num == 1 or num == 2:
        string = input('Введите текст\n')
        if num == 1:
            print('Выберите способ зашифровки текста:\n"1" - посимвольно\n"2" - по словам\n"3" - по блокам')
        else:
            print('Каким способом был зашифрован текст?\n"1" - посимвольно \n"2" по словам \n"3" - по блокам')
        numsec = input()
        numsec = int(numsec)
        code = input('Введите ключ (Каждое число должно вводиться через пробел)\n').split()
        if numsec == 1:
            pass
        elif numsec == 2:
            pass
        else:
            length = input('Введите длину блока\n')
            length = int(length)
    else:
        exit()
