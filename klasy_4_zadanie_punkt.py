# coding: utf-8

# Ukąś Pythona 6

# Zadanie Punkt/Koło -> (56min - END)

print " \n ------------- Zadanie Punkt/Koło - Wymagania rozpisujemy ------- \n "
#Wymagania sobie rozpisujemy:
#
# Proszę przygotować klasę która będzie definiować punkt na płaszczyźnie
# class Punkt:
#     def __init__(self, x, y):
#         pass  # ? -> Będzie definiować kilka metod
#
#     def odl_od_centrum(self):
#         pass  # ?
#         return odl  # float
#
#     def  odl_od_punktu(self, other):
#         pass  # ?
#         return odl  # float
#
# # Kolejna klasa to może byc koło
# class Kolo:
#     def __init__(self, x, y, r):
#         pass  # ?
#
#     def czy_wewnatrz(self, punkt):
#         # ?
#         return wynik  # bool


print " \n ------------- Zadanie Punkt/Koło - Robimy ------- \n "

class Punkt:  # Klasy przedewszystkim pomagają w pogrupowaniu metod
    def __init__(self, x, y):  # kontruktor tworzy nam atrybuty unikalne dla tego obiektu
        self.x = x
        self.y = y

    def  odl_od_punktu(self, other):
        odl = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return odl  # float

    def odl_od_centrum(self):
        #odl = (self.x**2 + self.y**2)**0.5
        #return odl  # float
        return self.odl_od_punktu(Punkt(0, 0))  # Lepiej, krócej i łatwiejŁatwiej -> wykożystać metode która już mamy a wiadomo że centrum to (0, 0)

class Kolo:
    def __init__(self, x, y, r):
        self.x = x  # wer. a
        self.y = y  # wer. a

        self.r = r
        ###
        #self.cntr = Punkt(x, y)  # wer. b -> krócej -> zamiast tych 2 pierwszych linijek -> potem tego użyć w metodzie czy_wewnatrz()

    def czy_wewnatrz(self, punkt):
        return punkt.odl_od_punktu(Punkt(self.x, self.y)) <= self.r  # wer. a
        ###
        #return self.cntr.odl_od_punktu(punkt) <= self.r  # wer. b -> krócej zamiast tej 1 linijki -> ale jeśli użuliśmy w konstruktorz -> self.cntr = Punkt(x, y)

# wywołanie
pkt1 = Punkt(0, 0)
pkt2 = Punkt(0, 0)

# sprawdzenie pobierzne -> w ramach treningu czy pkt1 to ten sam punkt pkt2
print pkt1 is pkt2  # False
print pkt1 == pkt2  # False
print pkt1.x == pkt2.x  # Porównanie wartości atrybutu x z obu punktów # True
print pkt1.y == pkt2.y  # Porównanie wartości atrybutu y z obu punktów # True

#wywołanie metody odl_od_centrum() na zmieniających się współrzędnych punktu pkt1
print " \n wywołanie metody odl_od_centrum() na zmieniających się współrzędnych punktu pkt1 --- "

print pkt1.odl_od_centrum()

pkt1 = Punkt(0, 1)
print pkt1.odl_od_centrum()

pkt1 = Punkt(0, 2)
print pkt1.odl_od_centrum()

pkt1 = Punkt(2, 0)
print pkt1.odl_od_centrum()

pkt1 = Punkt(3, 4)
print pkt1.odl_od_centrum()

pkt1 = Punkt(4, 4)
print pkt1.odl_od_centrum()  # Niby działa

#wywołanie metody odl_od_centrum() na zmieniających się współrzędnych punktu pkt1
print " \n wywołanie metody odl_od_centrum() na zmieniających się współrzędnych punktu pkt1 --- "

print pkt1.odl_od_centrum()  # Niby działa

pkt1 = Punkt(0, 1)
print pkt1.odl_od_centrum()  # Niby działa

pkt1 = Punkt(0, 2)
print pkt1.odl_od_centrum()  # Niby działa

pkt1 = Punkt(2, 0)
print pkt1.odl_od_centrum()  # Niby działa

pkt1 = Punkt(3, 4)
print pkt1.odl_od_centrum()  # Niby działa

pkt1 = Punkt(4, 4)
print pkt1.odl_od_centrum()  # Niby działa

#wywołanie metody odl_od_punktu() na 2 punktach
print " \n wywołanie metody odl_od_punktu() na 2 punktach --- "

cntr = Punkt(0, 0)  # utworzony próbnie
pkt1 = Punkt(1, 1)
print pkt1.odl_od_punktu(cntr)  # Niby działa

pkt2 = Punkt(4, 5)
print pkt1.odl_od_punktu(pkt2)  # Niby działa
print pkt2.odl_od_punktu(pkt1)  # Niby działa
print pkt1.odl_od_punktu(pkt1)  # Niby działa
