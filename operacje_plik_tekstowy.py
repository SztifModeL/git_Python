# coding: utf-8

# Ukąś Pythona 4

#Obsługa Plików txt -> (52min - END)


print " \n ------------- Obsługa plików txt ---------- \n "
# open('plit2.txt', 'x') - # Jest dopiero w Pythonie3
#open('plik.txt')  # Otwarcie pliu (domyslnie do odczytu)
#open('plik.txt', 'w')  # Utworzy plik jak nie istniał -> 'w' a jak isnieł to kasuje zawartość i otworzy do zapisu
#open('plik.txt', 'a')  # Otwiera w trybie append -> dopisuje do pliku nie kasując zawartości !!!
##
## Coś działamy
##
#plik.flush()  # Faktyczny zapis do pliku ale go nie zamyka
#plik.close()  # Zamyka i zapisuje

###################
#open('plik.txt')
#plik = open('plik.txt', 'w')
plik = open('plik.txt', 'a')  # Musimy nadac mu etykietę 'plik' = Zeby się odwoływac do otwierania pliku 'open('plik.txt')'
plik.write('Ala ma kota')  # .write() - zapisze dokładnie to co wstawimy bez żadnych dodatków ani enterów
plik.write('Kot ma pchły \n')
plik.write('Ala ma kota \n')
plik.write('Kot ma pchły')

imiona = ['Marcin', 'Tomek']  # Jakaś lista/tablica
plik.writelines(imiona)  # Dopisuje jakieś złożone żeczy jak tablice czy generatory
                         # Możemy np. Zapisywać do listy wyniki pomiarów co jakiś czas a funkcja będzie je zapisywała do pliku
plik.flush()  # Faktyczny zapis do pliku ale go nie zamyka
plik.close()  # Zamyka i zapisuje

print plik.closed  # Można sprawdzić czy jest zamnięty 'True' czyli zamknięty
print plik.encoding  #Domyślnie jest utf-8 ale mozna sprawdzić

print " \n ------ Bezpieczny ------- with - Bezpieczne otwieranie pliku - warancja zamknięcia i zapisu ---------- \n "
with open('plik.txt') as plik:  # otwórz poprzez 'with' plik 'plik.txt' i nadaj mu etykietę 'plik'
    print plik.readline()  # Wyswietli 1 linię (do pierwszego entera)
    print plik.readlines()  # Wyświetli wszystkie linijki
    print plik.read()  # Czyta całość tego co nie było czytane
    #  Dalsze operacje
print 'Koniec'  # Tutaj plik już jest zamknięty # Jak jest na równi z 'with' tzn że wszytsk poszło dobrze i plik jest zamknięty
