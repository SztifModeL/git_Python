# coding: utf-8

# Ukąś Pythona 3


#Funkcje - silnia rekurencyjna -> (56min - 1.12h)
#Funkcje - silnia iteracyjna -> (1.12h - 1.17h)
#Generator -> funkcjo podobny twór (1.17h - END)

print " \n ------------- Funkcje - Silnia rekurencyjna ----------------- \n "

# fact_rek -> po prstu faktoriał rekurencyjny -> po prostu taka nazwa

# definicja
def fact_rek(n):
    if n == 0:
        return 1
    else:
        return n * fact_rek(n-1)

# wywołanie:
print fact_rek(0)
print fact_rek(1)
print fact_rek(2)
print fact_rek(3)
print fact_rek(4)
print fact_rek(5)

print " \n ------------- Funkcje - Silnia rekurencyjna !!! zapis tej samej silni w 1 linijce !!! ----------------- \n "
def fact_rek2(n):
    return 1 if n == 0 else n * fact_rek2(n-1)  # Zapis zwrócenia i warunków w 1 linijce !!!

print fact_rek2(0)
print fact_rek2(1)
print fact_rek2(2)
print fact_rek2(3)
print fact_rek2(4)
print fact_rek2(5)

print " \n ------------- policz ilosc znaków np. z wyniku silni 100 ----------------- \n "
print fact_rek(100)  # pokaz wynik
print str(fact_rek(100))  # Zamień na string
print len(str(fact_rek(100)))  # Sprawdź długosć tringa
print len(str(fact_rek(998)))  # Sprawdź długosć tringa z max 998 # potem sie wywala ta funkcja, zależy od ilości dostępnej pamięci

print " \n ------------- Funkcje - Silnia Iteracyjna ----------------- \n "
def fact_iter(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

# wywołanie:
print fact_rek(0)
print fact_rek(1)
print fact_rek(2)
print fact_rek(3)
print fact_rek(4)
print fact_rek(5)

print " \n ------------- Generator wbudowany range() (generator liczb)----------------- \n "
print range(4)  # wyswietli 4 elementy
print type(range(4))  # Jakiego tyu jest range ? -> list -> nie tzreba żutowac na listę

for i in range(4):  # -> 1 ze sposobów na zrobienie sobie pętli o określonej liczbie iteracji
    print i

# w Pythonie3 tzreba to żutować na listę bo w P3 domyślnie range() jest krotką !!!
print list(range(2, 9))  # Można zmienić od kąd ma startowac i gdzie kończyć generowanie
print list(range(2, 9, 2))  # Można tez określic co która liczbę ma wygenerować, tu np. co drugą

print " \n ------------- Generator z funkcji ----------------- \n "
#Generator -> funkcjo podobny twór !!
def gen_ciag_liczb(n=0):
    while n < 100:
        print 'Debug -> Przed yield'
        yield n  # Jak 'return' zwaraca wartość ale nie wychodzi z funkcji tylko ją zawiesza | 'return' Zwraca i przerywa
        print 'Debug -> Po yield'
        n += 1  # Ten zapis znaczy tyle co n = n + 1

print gen_ciag_liczb()  # Nic jak by nie daje

# wywołanie:
x = gen_ciag_liczb()  # przypisanie zmiennej -> wywołaniu tego generatora

#wykożystanie generatora
for i in x:  # Przeiterowanie sie przez wywołany generator
    print i  # pokaże liczby wygenerowane