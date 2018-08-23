# coding: utf-8

# Ukąś Pythona 2

#lista -> (1-38 min) w pythonie to po prostu tablica
#Krotka -> (38-48 min) w pythonie to tablica zachowuje się jak lista ale w której nie można podmieniać wartości (niezmienialna)
#słownik -> (48 min - 1.20 min)w pythonie to lista asocjacyjna
#zbiób -> zbiór elementów które się nie powtarzają

print " \n ------------- Lista ----------------- \n "
# moja_lista = []
moja_lista = [1, 3.14, 'Ala ma kota']  #tworzę listę
print moja_lista

moja_lista.append(42)  # dodaje element na kniec moja_lista
print moja_lista

inna = [4, 5, 6]  # tworzy inna lista

moja_lista.extend(inna)  # dodaje iterowalne elementy do listy np. inną listę
print moja_lista

print moja_lista[0]  # wyśiwetlenie wartości o indexie 0

x = moja_lista[0]
print "Wartość listy o indexie 0 to:", x

moja_lista[3] = 111  # Wstawienie / Podmiana na miejsce index 3 wartości 111
print moja_lista

moja_lista.remove("Ala ma kota")  # Usuwa wartość z listy (trzeba wpisać wartośc listy a nie jej index)
print moja_lista

print len(moja_lista)  # pokaże długosc listy

print moja_lista[3:6]  # pokaże wycinek listy o indexach od 2 do 5

# Pętla przez wycinek listy -------------------------------
print "Pętla przez element wycinka listy"
for i in moja_lista[3:6]:
    print i
# ---------------------------------------------------------

moja_lista.pop()  # Usuwa element listy. bez indexu usuwa ostatni element
print moja_lista

moja_lista.extend(moja_lista)  # powiekszyłem listę o samą siebie
moja_lista.extend(moja_lista)  # powiekszyłem listę o samą siebie 2 raz
print moja_lista

moja_lista.pop(-1)  # usuwa element o indexie np. -1 czy li ostatni, każdy index może usunąć
print moja_lista

print moja_lista[2:10:2]  # pokaże wycinek listy o indexach od 2 do 10 ale co drugi (np. same odpowiedzi lub same pytania w rozmowie ;))

# Pętla ------------------------------------- przez wycinek tej listy żeby je wyświetlić ---------------
print "Pętla przez co drugi element wycinka listy"
for elem in moja_lista[2:10:2]:
    print elem
#-------------------------------------------------------------------------------------------------------

print moja_lista[::3]  # Wyswietli po prostu co trzeci element listy

print moja_lista[::-1]  # Wyswietli odwróconą kolejnośc listy

#
#
#####################----------- Krotka ---------------########################
#
#
print " \n ------------- Krotka ----------------- \n "
tuple()  # Tworzy pustą Krotkę

krotka = (5, 3.14, 42, 111, "Ala ma kota")  # widać że krotka bo jest w zwykłych nawiasach
krotka2 = 18, 33, 42  # Możliwy jest tez zapis krotki bez nawiasów (najwazniejszy jest ten przecinek, to on charakteryzuje to że jest to krotka)
print krotka
print krotka2

#
#
#####################----------- Słownik ---------------########################
#
#
print " \n ------------- Słownik ----------------- \n "

dict()  #Tworzy pusty Dictionary / Słownika = Lista asocjacyjna

d = {'Ala': 'kot', "Ola": "pies"}  #Tworzy słownik z dwoma itemami
#Item: Ala ma kota i item Ola ma psa
#Kluczu/index: 'Ala'
#Przypisana wartość 'kot'
print d

print d['Ala']  # pokaż wartoś -> odwołanie się do indexu

zwierzak = d['Ala']  # tworzę zmienna z indexu Ala
print zwierzak

imie = "Ala"  # tworzę zmienną po prostu string Ala
zwierzak = d[imie]  # tworzę zmienną na podstawie słownika i innej zmiennej
print zwierzak

# Jesli np zmienimy imie tzn. pobierzemy jakies inne
imie = "Ola"
zwierzak = d[imie]  # tworzę zmienną na podstawie słownika i innej zmiennej
print zwierzak

d['Tomek'] = 'pyton'  # tworzy nowy element słownika gdzie kluczem jest 'Tomek' a wartościa 'pyton'
print d

##################### Petla iterowanie w słowniku domyślnie po kluczach (bo jak mamy klucz to dostaniemy wartość)
print "\n Petla iterowanie w słowniku domyślnie po kluczach (bo jak mamy klucz to dostaniemy wartość)"
for i in d:
    print i  # Domyslnie słowniki iterują się po kluczach dlatego wyświetlił klucze

##################### Petla iterowanie w słowniku ale szukając wartości zaleznie od klucza
print "\n Petla iterowanie w słowniku ale szukając wartości zaleznie od klucza"
for i in d:
    print d[i]  # Domyslnie słowniki iterują się po wartościach dlatego wyświetli wartości
                # pokaż 'i' które przyjmuje każdy klucz słownika, wiec jak wyświetlimy d[i] to otrzymamy wartość

print d.items()  # pokaż itemy (paty: klucz + wartość)

##################### Petla iterowanie w słowniku po itemach tego słownika
print "\n Petla iterowanie w słowniku po itemach tego słownika"
for key, value in d.items():
    print key, value  # pokaż klucz i warość itemów -> rozpakuj item

##################### Rozpakowywanie listy na krotkę
print "\n Rozpakowywanie listy"
a, b, c = ['Michal', 'chomik', 'rybka']  # Po lewej krotka po prawej lista (jak wiecej elementów listy to wiecej elementów krotki)
print a
print b
print c

print d.keys()  # pokaż klucze

print d.values()  # pokaż wartości

##################### Update słownika
print "\n Update słownika"
print d

d.update({'Ola': 'chomik', 'Jacek': 'lew'})  #to co było zmieniło, a to czego nie było to dodało
print d

##################### Get słownika
print "\n Get słownika - unikanie błędu po zapytaniu o klucz który nie istnieje i nie dopisuje go do słownia"
print d['Tomek']  #czyli normalne zapytanie o wartoś klucza (mamy taki klucz)

#A jak nie mamy takiego klucza i wartości ?
#zwierzak = d.['Dominik']  #klucza 'Dominik' nie mamy
#print zwierzak  # wyskoczy błąd

#Możemy użyć Get żeby nie wyskoczył błąd po próbie wyświetlenia nie istniejącego klucza i umozliwia poznanie domyślnej wartości
d.get('Dominik', 'Brak Zwierza')  # Dominik nie występuje w kluczach ale jak będzie o niego zapytanie to domyślnie będzie 'Brak Zwierza' i nie wyskoczy błąd
                                  # Komenda nie dodaje Dominika do Słownika
                                  # Jak będzie pytanie o Tomka to dalej wyświetli ze słownika 'pytona' a nie brak zwierza
zwierzak = d.get('Dominik')
print zwierzak, "<- Brak błędu"

##################### Setdefault słownika # Robi to samo co get ale dopisuje do słownika
print "\n Setdefault słownika - unikanie błędu po zapytaniu o klucz który nie istnieje ale dopisuje go do słownia, może np. tworzyć domyślne ustawienia jakiegos programu"

d.setdefault('Dominik', 'papuga')
print d

######################################### Zbiór ###########################################################3
print " \n ------------- Zbiór ----- dostępne matematyczne operacje na zbiorach: dodawanie, odejmowanie, porównywanie itd.----- \n "

set()
print set()

zbiorek = set('Ala ma kota')  # tworzymy zbór
print zbiorek

zb_2 = set('Kot ma pchly')
print zb_2

print zbiorek.intersection(zb_2)  # pokaż część wspólną zbiorów

######################################### Copy -> na wszytskim działa -> lista, słownik, zbór ###########################################################3
print " \n ------------- Zbiór ----- dostępne matematyczne operacje na zbiorach: dodawanie, odejmowanie, porównywanie itd.----- \n "

##################### Copy -> na wszytskim działa -> lista, słownik, zbór
print "\n Copy -> na wszytskim działa -> lista, słownik, zbór"

li_1 = [1, 2, 3, 4]
li_2 = li_1

print li_1  # pierwsza lista
print li_2  # druga lista ale de fakto to ta sama tylko pod inną nazwa/etykietą

li_1[0] = 9

print li_1  # pierwsza lista
print li_2  # niby zminiliśmy tylko w pierwszej a w drugiej tez jest zmienione

# Trzeba użyć copy()
li_1 = [1, 2, 3, 4]
li_2 = li_1.copy()

print li_1  # pierwsza lista
print li_2  # juz 2 samodzielna lista -> tylko kopia pierwszej

####
#### Ale copy()
#### coś nie dział
####

