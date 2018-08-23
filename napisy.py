# coding: utf-8

# enter = "\n"
# tabulator = "\t"
# cudzyslow = "   \"   "
# apostrof = '   \'   '
#
# print enter, tabulator, cudzyslow, apostrof

# FORMATOWANIE NAPISÓW ------------------------------------
liczba = 5.25
podatek = 0.25

#napis = "Kwota do zapłaty:", liczba, "zł"  # niby działa ale wywala polskie znaki i jest w nawiasie

#napis = "Kwota do zapłaty: %s zł" %liczba  # znak %s zamienia na string, np. %d na decimal, %f na fluent itd... -> Nie ma problemów z polskimi znakami
napis = "Kwota do zapłaty: %s zł, podatek: %.2f zł." %(liczba, podatek)  # to samo co wyżej ale 2 zmienne z czeo druga jest jako zmienno pzrecinkowa z po przecinku mają byc 2 miejsca

print napis

