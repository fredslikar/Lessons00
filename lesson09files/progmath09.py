try:                                    # в блок трай мы помещает то, где может вызываться ошибка (например деления на 0)
    a = int(input("a:"))
    b = int(input("a:"))
    print (a/b)
except ZeroDivisionError:               # как бы пробовать кроме ошибки деления на 0, тогда - сообщение на 0 делить нельзя
    print("Na nol dilyty ne mogna!")

    



