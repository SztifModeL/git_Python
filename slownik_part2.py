# coding: utf-8

# Ukąś Pythona 3


#słownik -> (7min - 19min)w pythonie to lista asocjacyjna

print " \n ------------- Słownik ----------------- \n "
# Kluczem słownika nie może być ani lista ani zbiór -> Ale moga juz być wartościami
# Kluczem może być krotka bo jest niezmienna

d = {(0, 0): 'punkt centralny'}  # Tworzy słownik d
print d
print d[(0, 0)]  # pokaż wartość klucza (0, 0)

d[(0, 1)] = 'Inny punkt'  # Tworzy nowy element słownika gdzie kluczem jest (0, 1)
d[(1, 1)] = 3.14
d[(1, 0)] = ['Ala', 'ma', 'kota']
print d

print " \n ------------- Słownik -> Szukanie elemenu w słowniku  ----------------- \n "

print " \n Domyślnie szuka klucza a nie wartości ---"
d2 = {2: 'dwa', 3: 'trzy'}  # Tworzymy słownik o kluczach 2 i 3

print 2 in d2  # Jest to warunek loginczny -> Zwaraca True bo jest taki klucz
print 'dwa' in d  # Zwaraca False bo nie ma takiego klucza (jest taka wartość)

print " \n Szukanie w wartośćiach zamiast w kluczach ---"
print 'dwa' in d2.values()  # Jest to warunek loginczny -> Zwaraca True bo jest taka wartość

print " \n Szukanie klucza i odpowiadającej u wartości czyli całego itemu ---"
print (2, 'dwa') in d2.items()  # Jest to warunek loginczny -> Zwaraca True bo jest taki item


