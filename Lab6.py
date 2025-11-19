import random
def split(word, arg):
    y = []
    word += arg
    x = ""
    for u in word:
        if u != arg:
            x += u
        else:
            y.append(x)
            x = ""
    return y

def Mx(lt, arg):
    e = ""
    x = 0
    for n in lt:
        if len(n) > x:
            x = len(n)
            e = n
    if arg == "1":
        return e
    elif arg == "2":
        return x

#1
def Main1():
    r = str(input("Введите строку слов, разделённых пробелами: "))
    if r != "":
        print("Самое длинное слово: " + Mx(split(r, " "), "1"))
    else:
        print("Строка пустая, попробуйте еще раз.")
        Main1()

Main1()

Symb1 = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ"

#2
def Main2():
    r = str(input("Введите строку, которая содержит латинские буквы и отличные от них символы: "))
    len1 = 0
    len2 = 0
    for z in r:
        if not z in Symb1:
            len1 += 1
        else:
            if len2 < len1:
                len2 = len1
            len1 = 0
    print("Максимальная длина серии символов, отличных от латинских: " + str(len2))

Main2()

def abss(num):
    if num < 0:
        num = -num
    return num

nec = None
def nmin(lis):
    global nec
    t = 0
    for i in lis: t = i;break
    www = -1
    for y in lis:
        www += 1
        if t > y:
            t = y
            nec = www
    return t

#3
def Main3():
    n = input("Введите натуральное число: ")
    try:
        int(n)
    except:
        print("Неверное число, попробуйте еще раз.")
        Main3()
        return
    n = abss(int(n))
    list1 = [random.randint(-250, 250) for v in range(0, n)]
    sume = 0
    counte = 0
    for z in list1:
        if z > 0 and z % 5 == 0:
            sume += z
            counte += 1
    print("Сумма положительных элементов кратных 5: " + str(sume) + "\nИх количество: " + str(counte))
    print(list1)
    mine = nmin(list1)
    laste = 0
    for u in list1:
        laste+=1
        if laste == len(list1):
            laste = u
            break
    list1end = []
    xx = -1
    for mm in list1:
        xx += 1
        if xx == nec:
            list1end.append(laste)
        elif xx == len(list1) - 1:
            list1end.append(mine)
        else:
            list1end.append(mm)
    print(list1end)

Main3()
