# coding: utf-8

# Ukąś Pythona 3


#Funkcje -> (19min - 56min)

print " \n ------------- Funkcje ----------------- \n "

# typowa funkcja:
# definicja
def moja_funkcja(liczba1, liczba2):  # funkcja z parametrami (liczba1, liczba2) | funkcja która nie przyjmuje parametrów i tak musi mieć nawiasy -> moja_funkcja()
    #ciało funkcji
    #return wartość  # Zwykle zwraca jakąś wartość

    return liczba1 + liczba2

# wywołanie:
moja_funkcja(5, 7)
wynik = moja_funkcja(5, 7)  # Przechwycenie wartości -> przypisujemy ją do 'wynik'
print "wynik funkcji"
print wynik

print " \n ------------- Funkcje ze zmienną globalną ----------------- \n "
i = 7

def moja_funkcja(liczba1, liczba2):
    return i + liczba1 + liczba2

# wywołanie:
wynik = moja_funkcja(5, 7)  # Przechwycenie wartości -> przypisujemy ją do 'wynik'
print wynik

print " \n ------------- Funkcje z predefiniowanymi wartościami DOMYŚLNYMI ----------------- \n "
def dodawator(l1=1, l2=5):
    return l1 + l2

# wywołanie:
print dodawator(3)  # Podany tylo 1 parametr wiec wynik będzie 8 = 3 + 5

print " \n ------------- Funkcje z predefiniowanymi wartościami OBOWIĄZKOWYMI I DOMYŚLNYMI - 40min ----------------- \n "
def dodawator(l0, l1=1, l2=5):  # Najpierw wartości obowiązkowe potem domyślne -> Nie mozna mieszać!
    return l1 + l2

# wywołanie:
print dodawator(3)  # Podany tylo 1 parametr wiec wynik będzie 8 = 3 + 5

print " \n ------------- Funkcje ze zmianą jednej wartości domyślnej przy wywołaniu ----------------- \n "
def dodawator(l1=1, l2=5):  # Najpierw wartości obowiązkowe potem domyślne -> Nie mozna mieszać!
    return l1 + l2

# wywołanie:
print dodawator(l2=3)  # Zmiana tylko l2=3 wiec wynik będzie 4


print " \n ------------- Funkcja z nieograniczoną ilością parametrów ----------------- \n "
# *args - parametry krotki
# **kwargs - parametry słownika
def funkcyjka (par1, par2=5, *args, **kwargs):  # parametr obowiązkowy, parametr domyśny, *args - parametry krotki, **kwargs - parametry słownika
    print par1
    print par2
    print args
    print kwargs
    #return None  # Nic nie zwaracaj

# wywołanie:
print funkcyjka(1, 2, 3, 4, 5, 'test co wpadnie do krotki', tekst1='Ala ma kota - wpadnie do slownika bo ma klucz i wartosc', bla='blablabla' )
# Najpierw wysycił/pokazał podane paremetry zdefiniowane
# Resztę wstawił odpowiednio do krotki i słownika
# Mozna się przez nie się iterować i je tam znaleźć

print " \n ------------- Wywołanie tej samej funkcji z wczesniej przygotowanych parametrów ----------------- \n "
# wywołanie1:
print ' \n wywołanie1'
l = (1, 2, 3.14, 5)
print funkcyjka(l)  # Pod 'par1' wstawiło całe 'l'

# wywołanie2:
print ' \n wywołanie2'
print funkcyjka(*l)  # Rozpakowało po kolei wartości, 2 pierwsze wysyciło a nadwyżka trafiła do krotki

# wywołanie3:
print ' \n wywołanie3'
d = {'par1': 42, 'tekst': 'Ala ma kota'}
print funkcyjka(**d)  # Rozpakowało słownik w którym 'par1' = 42, par2 było definiowane = 5, reszta trafiła do dłownika

# wywołanie4:
print ' \n wywołanie4 ---> Krotkę można zamienic na listę list() i można to jakoś podmieniać i uwaktualniać bo krotki nie można zmieniać !!!'
l = (1, 2, 3.14, 5)
l = list(l)  # ---> Krotkę można zamienic na listę 'list()' i można to jakoś podmieniać i uwaktualniać bo krotki nie można zmieniać
print ' \n lista z l:'
print l

d = {'tekst': 'Ala ma kota'}  #usuniety 'par1' bo już dostał z 'l' i był by error
print funkcyjka(*l, **d)  # Rozpakowanie najpierw '*l' potem '**d' -> Wewnętrznie lista i tak jest zwracane jako krotka () i słownik {}