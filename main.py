def encryption(str_1, code_1, n_1):
    code_1 = list(map(int, code_1))
    lengthstr = len(str_1)
    lencode = len(code_1)
    if n_1 == 1:
        str_1 = str_1.ljust(lengthstr + (lencode - lengthstr % lencode) % lencode, "\0")
        lengthstr = len(str_1)
    count = int(lengthstr / lencode)
    a_1 = 0
    a_2 = lencode
    strsec = ''
    if n_1 == 2:
        for i in range(count):
            c = 0
            helps_1 = list(str_1[a_1:a_2])
            helps_2 = list(str_1[a_1:a_2])
            for j in code_1:
                helps_1[j] = helps_2[c]
                c += 1
            a_1 = a_2
            a_2 = a_2 + lencode
            strsec += ''.join(helps_1)
        while strsec[-1] == ' ':
            strsec = strsec[:-1]
    else:
        for i in range(count):
            helpstr = str_1[a_1:a_2]
            for j in code_1:
                strsec += str(helpstr[j])
            a_1 = a_2
            a_2 = a_2 + lencode
    return strsec


def encryption_2(str_2, code_2, n_2):
    code_2 = list(map(int, code_2))
    lengthcode = len(code_2)
    if n_2 == 1:
        str_2 = str_2.split()
        lengthstr = len(str_2)
        while len(str_2) != lengthstr + (lengthcode - lengthstr % lengthcode) % lengthcode:
            str_2.append('\0')
    elif n_2 == 2:
        str_2 = list(str_2.replace('  ', ' ').split(' '))
    lengthstr = len(str_2)
    count = int(lengthstr / lengthcode)
    a_1 = 0
    a_2 = lengthcode
    strsec = []
    strth = ''
    print(str_2)
    if n_2 == 2:
        for i in range(count):
            c = 0
            helps_1 = list(str_2[a_1:a_2])
            helps_2 = list(str_2[a_1:a_2])
            for j in code_2:
                helps_1[j] = helps_2[c]
                c += 1
            a_1 = a_2
            a_2 = a_2 + lengthcode
            strsec+=helps_1
        strth += ' '.join(strsec)
        while strth[-1] == ' ':
            strth = strth[:-1]
    else:
        for i in range(count):
            helpstr = str_2[a_1:a_2]
            for j in code_2:
                strsec.append(str(helpstr[j]))
            a_1 = a_2
            a_2 = a_2 + lengthcode
        strth = ' '.join(strsec)
    return strth


def encryption_3(str_3, code_3, n_3, length):
    code_3 = list(map(int, code_3))
    lengthcode = len(code_3)
    lengthstr = len(str_3)
    count_symbols = (length - lengthstr % length) % length + ((lengthcode - lengthstr % lengthcode) % lengthcode)
    str_3 += '\0' * count_symbols
    lengthstr = len(str_3)
    block = ''
    temporary = length
    strsec = []
    for i in range(lengthstr):
        if temporary == 0:
            strsec.append(block)
            block = ''
            temporary = length
        block += str_3[i]
        temporary -= 1
    strsec.append(block)
    lengthstr = len(strsec)
    count = int(lengthstr / lengthcode)
    a_1 = 0
    a_2 = lengthcode
    strth = ''
    strf = []
    if n_3 == 2:
        for i in range(count):
            c = 0
            helps_1 = list(strsec[a_1:a_2])
            helps_2 = list(strsec[a_1:a_2])
            for j in code_3:
                helps_1[j] = helps_2[c]
                c += 1
            a_1 = a_2
            a_2 = a_2 + lengthcode
            strf += helps_1
        strth += ''.join(strf)
        while strth[-1] == ' ':
            strth = strth[:-1]
    else:
        for i in range(count):
            helpstr = strsec[a_1:a_2]
            for j in code_3:
                strth += str(helpstr[j])
            a_1 = a_2
            a_2 = a_2 + lengthcode
    return strth


def codechecking(code_1):
    if len(code_1) == 0:
        print('Данные не были введены.')
        return False
    else:
        try:
            code_1 = list(map(int, code_1))
        except ValueError:
            print('Были введены некорректные данные. (Ключ должен состоять из чисел)')
            return False
        maxc = max(code_1)
        if len(set(code_1)) != maxc + 1:
            print('Были введены некорректные данные. (В ключе пропущены числа или есть повторяющиеся.)')
            return False
        return True


def numberchecking(n):
    if len(n) == 0:
        print('Данные не были введены.')
        return False
    else:
        try:
            n = int(n)
        except ValueError:
            print('Были введены некорректные данные. Вернемся в начало. ')
            return False
    if n != 0 and n != 1 and n != 2:
        return False
    return True


def stringchecking(str_1):
    if len(str_1) == 0:
        print('Данные не были введены.')
        return False
    return True


def bcheking(b_1):
    if len(b_1) == 0:
        print('Данные не были введены.')
        return False
    else:
        try:
            b_1 = int(b_1)
        except ValueError:
            print('Были введены некорректные данные. Вернемся в начало.')
            return False
    if b_1 != 1 and b_1 != 2 and b_1 != 3:
        return False
    return True


def lengthcheking(length_1):
    if len(length_1) == 0:
        print('Вы ничего не ввели.')
        return False
    else:
        try:
            length_1 = int(length_1)
        except ValueError:
            print('Были введены некорректные данные. Вернемся в начало.')
            return False
    return True


print('Добро пожаловать в приложение для шифрования и дешифровки текста - "ENCRY".')
while True:
    print('Для зашифрования текста введите "1"\nДля дешифровки введите -"2"\nДля выхода из приложения - "0"')
    n = input()
    if numberchecking(n):
        n = int(n)
        if n == 1 or n == 2:
            string = input('Введите текст\n')
            if stringchecking(string):
                if n == 1:
                    print('Выберите способ зашифровки текста:\n"1" - посимвольно\n"2" - по словам\n"3" - по блокам')
                else:
                    print('Каким способом был зашифрован текст?\n"1" - посимвольно \n"2" по словам \n"3" - по блокам')
                z = input()
                if bcheking(z):
                    z = int(z)
                    code = input('Введите ключ (Каждое число должно вводиться через пробел)\n').split()

                    if codechecking(code):
                        if z == 1:
                            print(encryption(string, code, n))
                        elif z == 2:
                            print(encryption_2(string, code, n))
                        else:
                            lenb = input('Введите длину блока\n')
                            if lengthcheking(lenb):
                                lenb = int(lenb)
                                print(encryption_3(string, code, n, lenb))
        else:
            exit()

