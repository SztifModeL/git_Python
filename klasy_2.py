# coding: utf-8

# Ukąś Pythona 6

# Klasy_2 -> (0min - 31min)

#atrybut to jest tylko nazwa -> karteczka przylepiona do jakiegoś obiektu

print " \n ------------- Klasy_2 - ogólnie --------- \n "
class Osoba(object):
    ile = 0  # atrybut klasy jeśli go zmienimy to w obiektach też się zmieni !!!

    def __init__(self, imie, *args, **kwargs):  # konstruktor
        self.imie = imie  # unikalny atrybut obiektu
        self.wiek = 30
        Osoba.ile += 1  # zliczamy populację osób -> odwołanie sie bezpośrednio do atrybutu w klasie

    def metoda():  # funkcja w klasie
        def funkcja(parametr):  # funkcja wewnątrz funkcji -> Dekorator o czym będzie rozmowa póżniej
            return parametr+1
        return funkcja

    class Wewnetrzna(object):  # wewnątrz klas możemy twożyć tez inne klasy do użytku wewnętrznego
        pass

print Osoba.ile

obj = Osoba('Tomek')  # wywołanie instancji -> tym samym stworzenie obiektu

print obj.imie  # wyświetlenie -> ten nasz 'obj' ma wewnątrz zapisany atrybut 'imie' z którym jest powiązana wartość 'Tomek'
print 'Jest nas:', obj.ile

print obj.ile  # 'obj' otrzymał wartość która była zapisana wewnątrz klasy =0

Osoba.ile = 2  # zmieniłem wartość atrybutu 'ile' z 0 na 2 co niesie ze sobą konsekwencje że obiekty też bądą miały ją zmienioną
print obj.ile  # juz ma zmienioną wartość =2

print " \n ------------- Czy obiekt jest instancją klasy --------- \n "
isinstance(obj, Osoba)  # najpierw nazwa ojektu, potem nazwa klasy -> zwraca True/False
print isinstance(obj, Osoba)

print " \n ------------- Czy obiekt posiada jakiś atrybut --------- \n "
hasattr(obj, 'ile')
print hasattr(obj, 'ile')  # wyszło True -> object 'obj' posiada atrybut 'ile'
print hasattr(obj, 'suma')  # wyszło False

print " \n ------------- getattr --------- \n "
# bierze atrybut obiektu i można z nim coś zrobić np. zmienić mu nazwę
print getattr(obj, 'ile')  # jesli wezmę 'getattr' atrybutu 'ile' to dostane wartosć =2
i = getattr(obj, 'ile')
print i  # pokaż wartość identyfikatoa 'i' pokaże =2

######

i = 3 # Jaśli identyfikatorowi 'i' przypiszemy wartość 3 -> to nie zmieni to wartości (po prostu teraz 'i' przyczeione jest do wartości 3
print obj.ile  # Dalej jest =2
