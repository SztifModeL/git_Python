# coding: utf-8

# Ukąś Pythona 5

# Klasy -> (60min - END)


print " \n ------------- Klasy info ---------- \n "
# Schemat obiektów które będziemy tworzyć

class NaszaKlasa(object):  # Klasa -> może byc też bez (object) -> class NaszaKlasa:
    #atrybut_klasy = 7  # Atrybut klasy

    # Kontruktor -> __init__(self) -> Unikalne rzeczy dla obiektów mousimy zrobić w konstruktorze
    def __init__(self, param, *args, **kwargs):  # self - ten właśnie obiekt który w tym momencie jest tworzony i przekazywany do konstruktora
                                                # parametr domyślny którego nigdy nie podajemy ręcznie (na liście argumentów)
                                                # jest on podawany od automatycznie przy wywoływaniu metody
        self.etykieta = param  # w obiekcie self utwórz etykietę imie i przypisz ją do wartości przekazanej pzrez parametr -> Przejecie tego co było przekazane przez parametr i zapisanie tego do wewnątrz obiektu

    # Destruktor
    def __del__(self):
        print 'Słabo mi...'

# Przykład
print " \n Klasa1 -- Osoba --- "

class Osoba:
    def __init__(self, imie='Bezimienny'):  # 'imie' -> domyślny parametr który potem nadpisujemy
        self.imie = imie
    def __del__(self):
        print 'obiekt', self.imie, 'mówi: Słabo mi...'  # Zapis w od razu z nazwą obiektu usuwanego
        # print 'Słabo mi...'  # Po prostu coś, żeby wyło wiadomo żę destruktor zadziałał

jan = Osoba('Jan')  #wywołanie instancji -> tym samym stworzenie obiektu

print jan.imie  #wyświetlenie -> ten nasz 'jan' ma wewnątrz zapisany atrybut 'imie' z którym jest powiązana wartość 'Jan'

del jan  #Usuwanie etykiety/obiektu - > usunięcie etykiety wiąże się najczęsciej z usunięciem obiektu po prostu przez Garbage Kolektor






