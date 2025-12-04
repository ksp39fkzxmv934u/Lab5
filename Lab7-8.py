import random

def SUMlist(listt):
    cntrl = 0
    for i in listt:
        cntrl += i
    return cntrl

def ShowMatrix(listt):
    r = ""
    for g in listt:
        r += str(g) + str("\n")
    return r

def SortInc3(A, B, C):
    t = [A,B,C]
    for _ in range(0, 2):
        for v in range(0, 2):
            if t[v] > t[v + 1]:
                t[v], t[v + 1] = t[v + 1], t[v]
    return t

Haha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ"

#1
print("Задание 1.")
def Main1():
    N = input("Введите натуральное число(N): ")
    try:
        N = int(N)
    except:
        print("Попробуйте еще раз.")
        Main1()
        return
    if int(N) <= 0:
        print("Попробуйте еще раз.")
        Main1()
        return
    M = input("Введите натуральное число(M): ")
    try:
        M = int(M)
    except:
        print("Попробуйте еще раз.")
        Main1()
        return
    if int(M) <= 0:
        print("Попробуйте еще раз.")
        Main1()
        return

    list1 = [[random.randint(0,100) for _ in range(0, M)] for _ in range(0, N)]
    print("1. \n" + ShowMatrix(list1))
    S = [SUMlist(s) for s in list1]
    print("2. " + str(S))

Main1()

#2
print("Задание 2.")
def Main2():
    print("Введите числа для первого набора чисел:")
    A1 = input("A1: ")
    try:
        A1 = float(A1)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return
    B1 = input("B1: ")
    try:
        B1 = float(B1)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return
    C1 = input("C1: ")
    try:
        C1 = float(C1)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return
    print("Введите числа для второго набора чисел:")
    A2 = input("A2: ")
    try:
        A2 = float(A2)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return
    B2 = input("B2: ")
    try:
        B2 = float(B2)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return
    C2 = input("C2: ")
    try:
        C2 = float(C2)
    except:
        print("Попробуйте еще раз.")
        Main2()
        return

    E1 = [A1, B1, C1]
    E2 = [A2, B2, C2]
    print("1. (" + str(E1[0]) + ", " + str(E1[1]) + ", " + str(E1[2]) + "), " + "(" + str(E2[0]) + ", " + str(E2[1]) + ", " + str(E2[2]) + ")")
    E1S = SortInc3(E1[0], E1[1], E1[2])
    E2S = SortInc3(E2[0], E2[1], E2[2])
    print("2. (" + str(E1S[0]) + ", " + str(E1S[1]) + ", " + str(E1S[2]) + "), " + "(" + str(E2S[0]) + ", " + str(E2S[1]) + ", " + str(E2S[2]) + ")")

Main2()

print("Задание 3.")
def Main3():
    a = str(input("Введите любую строку, содержащую буквы: "))
    b = {}
    for y in a:
        if y in Haha:
            if not b.get(y):
                b[y] = 1
            else:
                b[y] += 1
    if b == {}:
        print("Попробуйте еще раз.")
        Main3()
        return
    print(b)
    while True:
        c = str(input("Введите букву из этой строки: "))
        if b.get(c):
            print("Количество '" + c + "' в этой строке: " + str(b.get(c)))
            break
        else:
            print("Данного символа нету в этой строке, попробуйте еще раз.")

Main3()
