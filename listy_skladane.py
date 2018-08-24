# coding: utf-8

# Ukąś Pythona 4


#listy składana -> (25min - 36min)


print " \n ------------- listy składane  ----------------- \n "


print " \n Lista - wyciąganie określonych danych z listy w której są słowniki z kluczami jak np. w DB---------- "
# Np. Dostaliśmy listę id i imion z bazy danych
# Chcemy tylko listę imion

lista = [{'imie': 'Jan', 'id': '1'},
         {'imie': 'Tomasz', 'id': '2'},
         {'imie': 'Dominik', 'id': '3'}]

print " \n zapis zwykły 3 linijki ---"
imiona = []  #Tworzymu pusta listę na imiona
for d in lista:
    imiona.append(d['imie'])  # W każdej iteracji pętli-> Dopisywane jest to co jest pod kluczem 'imie'

print imiona  # pokaże wynik w postaci listy
for i in imiona:  # Przeiteruje sie przez listę i wypisze wyniki
    print i

print " \n zapis skrócony do 1 liniki ---"
imiona = [d['imie'] for d in lista]  # imiona = [] <- Nawiasy [] mówią że to będzie lista
                                     # d['imie'] <- to co będziebędzie wstawiane do listy
                                     # for d in lista <- potem tylko pętla for
for i in imiona:  # Przeiteruje sie przez listę i wypisze wyniki
    print i

print " \n zapis skrócony do 1 liniki + warunki ---"
# Pokaże imiona dla nieparzystych id
# Inaczej -> Chce dostać 'imie' z każdego elementu znajdującego się w liście, jeżeli reszta z dzielenia nr 'id' jest równa 1 ( jest nieparzyste)
imiona = [d['imie'] for d in lista if int(d['id']) % 2 == 1]
# Opis -> Stwórz mi listę zawierającą wartość wyciągnieta z klucza 'imie'
# z obiektu 'd'
# dla każdego 'd' znajdującego sie w liscie
# Sam Ddałem !!! -> rzutowanie na int
# lieżeli wartość wyciągnieta z podklucza id z tego elementu modulo 2 będzie równe 1

for i in imiona:  # Przeiteruje sie przez listę i wypisze wyniki
    print i

