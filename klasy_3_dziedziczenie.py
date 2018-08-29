# coding: utf-8

# Ukąś Pythona 6

# Dziedziczenie -> (31min - 56min)
# Python przeszukuje listę klas pierwotnych by znaleźć metode w takiej kolejności w jakiej podaliśmy

print " \n ------------- Klasy_3 - Dziedziczenie tworzenie klas pochodnych --------- \n "

class Osoba(object):
    ile = 0
    def __init__(self, imie, nazwisko):  # konstruktor
        self.imie = imie
        self.nazwisko = nazwisko

    def przywitanie(self):  # 'przywitanie' -> Metoda do wykonanie na obiekcie -> która będzie dziedziczona
        print 'Hej, nazywam się', self.imie, self.nazwisko

class InnaKlasa:
    ile = 1
    def przywitanie(self):  # Specjalnie tak samo się nazywa metoda żeby sprawdzić z której odziedziczy ;)
        print 'Jestem z Innej Klasy'

class JeszczeInnaKlasa:
    ile = 2
    def przywitanie(self):  # Specjalnie tak samo się nazywa metoda żeby sprawdzić z której odziedziczy ;)
        print 'Jestem z Innej Klasy'

# Chcę oprócz tego że Pracownik ma 'imie' i 'nazwisko' to żeby jescze miał 'stanowisko' -> wiec dziedziczy z 'Osoba'
class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, stanowisko):  # Możemy sobie zredefiniować w konstruktorze -> czyli wpisac jeszcze raz te parametry
        #self.imie = imie  # Można ale żeby nie przepisywac znów z Osoby
        #self.nazwisko = nazwisko  # Można ale żeby nie przepisywac znów z Osoby
        super(Pracownik, self).__init__(imie, nazwisko)  # W Pythonie2 - > super(<nazwa_tej_klasy>, self).__init__(<parametry_które chcemy>) -> Jak będzie dziedziczył z kilku klas to będzoe sprawdzał je w kolejności wpisania
        # Osoba.__init__(self, imie, nazwisko)  # Analogiczne wywołanie gdy nie użyjemy tego wyżej -> ale jest różnica że tu wpisujemy ktura metodę z której klasy używamy
        # super()  # W Pythonie3 -> wystarczy samo super()
        self.stanowisko = stanowisko


# Chcę oprócz tego że Student ma 'imie' i 'nazwisko' to żeby jescze miał np 'wysokosc_stupendium' czy 'srednia_ocen' czy 'rocznik'
class Student(Osoba, InnaKlasa, JeszczeInnaKlasa):
    pass

    def przywitanie(self):
        super(Student, self).przywitanie()  #Jak będzie dziedziczył metode z kilku klas to będziee szukał w klasach w kolejności wpisania -> class Student(Osoba, InnaKlasa, JeszczeInnaKlasa):
        # super().przywitanie()  # w Pythonie3 już skrócili zapis
        #InnaKlasa.przywitanie(self)  # Można na sztywno wpisać z której klasy ma dziedziczyć że z 'InnaKlasa' a nie pierwszej tj 'Osoba' -> ale nie jest to dobra praktyka -> ale można ;) !!!

#### Tworzymy obiekty
prac1 = Pracownik('Jan', 'Kowalski', 'portier')
stu1 = Student('Tomasz', 'Iksiński')

#### Sprawdzamy do jakiej klasy należą obiekty
print isinstance(prac1, Osoba)  # czy należy do klasy Osoba ? = True
print isinstance(prac1, Student)  # czy należy do klasy Student ? = False

#### Sprawdzamy wartości atrybutów
print prac1.imie  # pokaż wartośc atrybutu imie w obiekcie prac1
print prac1.nazwisko
print prac1.stanowisko

print " \n Tworzymy obiekt i odpalamy na nim metodę - która zadziała ? którą odziedziczy ? --- "
student = Student('Jan', 'Kowalski')
student.przywitanie()  # Wyśietlił bo w metodzie był print -> Hej, nazywam się Jan Kowalski
# Ale jak zmienimy w Studencie kolejnosc dziedziczenia na:
# class Student(InnaKlasa, JeszczeInnaKlasa, Osoba):
# to pierwsza metoda 'przywitanie()' będzie z klasy 'InnaKlasa
# czyli wyświetli -> Jestem z Innej Klasy
# można to obejść i na sztywno wpisać z której klasy ma dziedziczyć że z 'InnaKlasa' a nie pierwszej tj 'Osoba'
# nie jest to dobra praktyka -> ale można ;) !!!
# InnaKlasa.przywitanie(self)

print " \n Tworzymy obiekt i sprawdzamy wartośc atrybutu 'ile' - którą odziedziczył ? --- "
student = Student('Jan', 'Kowalski')
student.ile
print ' atrybut ile ma wartość ->', student.ile, '-> Bo odziedziczył wartość atrybutu po klasie Osoba'
