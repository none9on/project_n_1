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
