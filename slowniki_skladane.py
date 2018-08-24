# coding: utf-8

# Ukąś Pythona 4

#Słowniki składane -> (36min - 42min)


print " \n ------------- Słowniki składane  ----------------- \n "
# Np. Dostaliśmy listę id i imion z bazy danych
# Chcemy zrobić Słownik w ktorym kluczem będzie index danego imienia w tej liście
lista = [{'imie': 'Jan', 'id': '1'},
         {'imie': 'Tomasz', 'id': '2'},
         {'imie': 'Dominik', 'id': '3'}]

print " \n enumerate -> poindexowane wartości listy ---"
print enumerate(lista)  # Samo wyświetlenie pokazuje kaszaki -> że to jakiś generator -> wiec tzreba się pzrez to przeiterować pętlą for
for elem in enumerate(lista):
    print elem  # Teraz widzimy że mamy poindexowane wartości z 'lista' (wartościami w tej liście były słowniki)

print " \n Tworzymy nasz słownik ---"
tmp = {i: d['imie'] for i, d in enumerate(lista)}
# i: -> Co ma byc kluczem
# d['imie'] -> Sposób na wyciągniecie wartości która będzie przypisana kluczowi
# for i, d -> Pętla for która dostaje 2 wartości

print tmp  # Pokaż -> Słownik składany z indexu wartości lsty i imienia wyciągnietego z tych wartości



