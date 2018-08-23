# coding: utf-8

# if warunek :
#     blok kodu wykonywany, gdy warunek jest spełniony
# elif inny_warunek :
#     blok kodu wykonywany, gdy warunek nie jest spełniony ale inny_waruek jest spełniony
# else :
#     blok kodu wykonywany, gdy żaden z wcześniejszych warunków nie został spełniony


# PROG 1 -------------------------------------------------
# liczba = 7            # wartośc nadawana programowo wiec wiadoo
#
# if liczba % 2 == 0:
#     print "Liczba", liczba, "jest parzysta"  # wyświetlenie str i int w jednym princie
# elif liczba % 2 == 1:
#     print "Liczba", liczba, "jest nieparzysta"
# else:
#     print "Liczba", liczba, "jest dziwaczna"


# PROG 2 ------------ liczba podawana z klawiatury --------------

liczba = input("Podaj liczbę: ") # wartośc podawana z klawiatury
print (type(liczba))  # sprawdzanie typu wpisanej frazy

if liczba % 2 == 0:
    print "Liczba", liczba, "jest parzysta"  # wyświetlenie str i int w jednym princie
elif liczba % 2 == 1:
    print "Liczba", liczba, "jest nieparzysta"
else:
    print "Liczba", liczba, "jest dziwaczna"
