# coding: utf-8

# Ukąś Pythona 5

# Moduły -> (33min - 60min)


print " \n ------------- Import Modułu wewnętrznego z pythona ---------- \n "
import datetime # Import wbudowanych modułów (tu od czasu)

teraz = datetime.datetime.now()  # wywołanie metody .now() pokaże date i czas z dokładnością do milionowej częsci secundy
wtedy = datetime.datetime(2018, 7, 15, 7, 51, 32)  # Wprowadzana data musi być w określony sposób
delta = (teraz - wtedy)  # Nadanie jakiejś zmiennej -> Oparacja różnicy/odjęcia dat
print delta
print delta.days  # żeby pokazała ile to dni

print " \n ------------- Import tylko części/funkcji z Modułu ---------- \n "
#Składnia
#from <nazwa_modułu> import <funkcja/klasa/submoduł> as <nowy_id>
from datetime import datetime as dt
print dt.now()

print " \n ------------- Import modułu z pliku w którym jest tylko ten moduł ---------- \n "
# Plik z modułem nie może mieć nazwy 'test' ani 'import'

# importowany jest cały plik -> wykonymany jest cały plik od początku do konca !!!
# dopiero jak on się cały wykona prawidłowo
# to wyłuskiwane są wszytskie obiekty które tam były -> wybierany jest ten który my potzrebujemy i reszta jest usuwana

print " \n ------------- Import modułu z naszego pliku ale wktórym są różne obiekty ---------- \n "
# Plik z modułem nie może mieć nazwy 'test' ani 'import'

# --> Dzięki __name__ Możemy wtedy zrobić funkcję która będzie różnie odpalać nasz plik z modułem
# Jesli odpalamy program normalnie z linii poleceń czy okienkowo to jego __name__ == '__main__'
# ale jesli go importuje to przyjmuje on __name__ = <program pliku importowanego>

# --> zabezpieczenie odpalenia jako moduł -> # Może być ale nie musi jaśli cały plik to tylko sam moduł
# To poniżej używamy w pliku z modułem tak jak w tym przypadku ->
if __name__ == '__main__':
    print 'Nazywam się: ', __name__, 'i działam jako program'
else:
    print 'Nazywam się: ', __name__, 'i działam jako wczytany moduł'

# Zalecenie: -> w P3 już nie aktualne
# Jeśli jakis katalog miał byc traktowany jak moduł -> trzeba było utworzyc plik '__init__.py' (może być pusty)

#Import modułu
from modul import plik_z_modulem_do_wgrania

print " \n ------------- Inne ciekawe wbudowane moduły ---------- \n "
# datetime # już był teraz
# random
# calendar
# http
# os  # podobno będzie
# sys  # podobno będzie

print " \n ------------- Moduły spoza wbudowanych i naszych - znalezione ;) --------- \n "
# Trzeba je zainstalować managerem pakietów, najlepiej 'pip' ('easy_instal' - jakiś stary manager)
# pip
# https://pypi.python.org/ -> biblioteka wszytskich zewnętrzna modułów z których kożysta pip
# pip instal <nazwa_modułu>




