import math


def fel1():
    print("1.feladat")
    szam: int = int(input("Adjon egy pozitív egész számot !"))
    i = 0
    while szam < 0:
        szam: int = int(input("A számnak egy pozitív egész számot kell meg adni!"))
    while i <= szam:
        if i == szam:
            print(i, end="")
        else:
            print(i, end=";")
        i += 1


def fel2():
    print("2.feladat")
    i = 1
    osszeg = 0
    szam: int = int(input("Adjon egy pozitív egész számot !"))
    while szam < 0:
        szam: int = int(input("A számnak egy pozitív egész számot kell meg adni!"))
    while i < szam:
        if szam % i == 0:
            print(i, end=" ")
            osszeg += i
        i += 1
    print(f"\n{osszeg}")


def fel3():
    print("3.feladat")
    csere: int = 0
    szam1: int = int(input("Adjon egy pozitív egész számot !"))
    szam2: int = int(input("Adjon egy pozitív egész számot !"))
    while szam1 < 0 or szam2 < 0:
        szam1: int = int(input("A számnak egy pozitív egész számot kell meg adni!"))
        szam2: int = int(input("A számnak egy pozitív egész számot kell meg adni!"))
    if szam1 > szam2:
        csere = szam2
        szam2 = szam1
        szam1 = csere

    while szam1 < szam2:
        if szam1 % 2 == 0:
            if szam1 == szam2-2:
                print(szam1, end="")
            else:
                print(szam1, end=",")
        szam1 += 1


def fel4():
    print("4.feladat")
    i = 1
    while i <= 20:
        if i == 20:
            print(f"{math.pow(i, 2):.0f}", end="")
        else:
            print(f"{math.pow(i, 2):.0f}", end=",")
        i += 1


def fel5():
    print("5.feladat")
    i = 0
    szoveg = input("Adjon egy szöveget!")
    while i < len(szoveg):
        print(szoveg[i])
        i += 1


def fel6():
    print("6.feladat")
    szoveg = input("Adjon egy szöveget!")
    i = len(szoveg)
    while i > 0:
        print(szoveg[i-1])
        i -= 1


def fel7():


