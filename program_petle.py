# coding: utf-8

#-------------------------- PĘTLE --------------------------#

# while warunek :
    # blok kodu
    # blok kodu

# Pętla 1 ---------------------------------------------------

liczba = 1  # wykonuje sie, jak długo spełniony jest warunek

while liczba < 10:
    print "Python jest spoko! Liczba jest równa:",liczba,"i jest mniejsza od 10"
    liczba = liczba + 1  # za każdym razem zwiekszamy liczba + 1

# Pętla 2 ---------------------------------------------------

# while True:  # pętla nieskończona, wykonuje się w nieskończoność, zatrzyma się po porawnej odpowiedzi
#     liczba = int(input("Podaj liczbę parzystą: "))
#
#     if liczba % 2 == 0:
#         print "Brawo!"
#         break  # break zatrzymuje pętlę
#
#     else:
#         print "Skup się! PARZYSTA!"