# coding: utf-8

# Plik z modułem nie może mieć nazwy 'test' ani 'import'

# --> zabezpieczenie odpalenia jako moduł -> # Może być ale nie musi jaśli cały plik to tylko sam moduł
# To poniżej używamy w pliku z modułem tak jak w tym przypadku ->
if __name__ == '__main__':
    print 'Nazywam się: ', __name__, 'i działam jako program'
else:
    print 'Nazywam się: ', __name__, 'i działam jako wczytany moduł'

# --> reszta modułu:
def wczytaj_od_usera():
    '''
    Funkcja ma za zadanie pobierac od uzytkowanika napis i zapisywac go do pliku.
    1. Po wprowadzniu stringa i eneterze zapisuje
    2. A po samym eneterze miał zatrzymać i wyświetlić a wywala błąd !!!
    '''
    napis = str(input('Podaj napis do zapamiętania: '))
    with open('plik_z_danymi.txt', 'a') as plik:
        while napis:
            plik.write(napis + '\n')
            napis = str(input('Podaj napis do zapamiętania: '))
    print 'Dzięki za współpracę'

def wczytaj_z_pliku():
    '''
    Funkcja wczytuje z pliku kolejne linijki i zwraca słownik w tórym kluczem jest numer linii a wartością zawartość tej linii.
    '''
    with open('plik_z_danymi.txt', 'r') as plik:
        linijka = plik.readlines()
        result = {idx+1: linia.strip() for idx, linia in enumerate(linijka)}  # idx jest +1 bo normalnie jest numerowany od 0.
        #print type(result)
        print result
    return result

# wywołanie #Komentuje żeby mnie ciąle nie pytało
# wczytaj_od_usera()
wczytaj_z_pliku()

print " \n Strip usuwa białe znaki z początku i z końca --- "
#Wyjaśnienie '.strip()' użyte powyżej !!!
# d = wczytaj_z_pliku()
# napis = d[2]
# print napis  # Nie widać ale p tych 888 było '\n'
# print napis.strip() # Strip usuwa białe znaki: spacje, tabulatory, entery itd. z początku i z końca napisu (wszelkie wewnętrzne zostają)









