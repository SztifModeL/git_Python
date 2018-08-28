# coding: utf-8

# Ukąś Pythona 4

#Lista Sort -> (ok50min)


print " \n ------------- lista.sort  -------przy po mocy lambdy---------- \n "
# Trzeba podać po czym ma sortowac listę (w tym wypadku słowników)
lista = [{'imie': 'Jan', 'id': '1'},
         {'imie': 'Tomasz', 'id': '2'},
         {'imie': 'Dominik', 'id': '3'}]

print lista  # Normalnie nie posortowana

lista.sort(key=lambda d: d['imie'])  # Jedno argumentowa funkcja lambda która wyciąga imie i używa go jako klucz sortowania)
print lista  # Posortowana

print " \n ------------- lista.sort  ------- normalnie ---------- \n "
# Trzeba podać po czym ma sortowac listę (w tym wypadku słowników)
lista = [{'imie': 'Jan', 'id': '1'},
         {'imie': 'Tomasz', 'id': '2'},
         {'imie': 'Dominik', 'id': '3'}]

def f(d):  # Funkcja 'f' zwracająca imie
    return d['imie']

lista.sort(key=f)  # Sortowanie po jakimś kluczu (trzeba go określić - tu wybraliśmy imie)

print lista