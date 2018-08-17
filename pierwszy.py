# -*- coding: utf-8 -*-

print("Ahoj, Przygodo!")
print('Cześć')


rok1 = 2017
rok2 = 2019
rok3 = 2021


# jedna zmienna
print("Ten odcinek powstal w {} roku".format(rok1))

# kilka zmiennych z indexem kolejnosci w nawiasie na koncu
print("Ten odcinek powstal w {0} roku a nie w {1} roku".format(rok2, rok3))

# kilka prostych zmiennych z nazwa zmiennej
print("Ten odcinek powstal w {rok3} roku".format(rok3=rok3))

# program pole / obwod
"""
wysokosc = 5
szerokosc = 7

pole = wysokosc * szerokosc
obwod = 2 * (wysokosc + szerokosc)

print("Pole wynosi", pole)
print("Obwod wynosi", obwod)
"""

# program pole / obwod z INPUT zbiorczy zapis
"""
wysokosc = float(input("Prosze podac wysokosc prostokata "))
szerokosc = float(input("Prosze podac szerokosc prostokata "))

pole = wysokosc * szerokosc
obwod = 2 * (wysokosc + szerokosc)

print("Pole wynosi {}".format(pole))
print("Obwod wynosi {}".format(obwod))
"""

# program pole / obwod z INPUT
print("Prosze podac wysokosc prostokata ")
wysokosc = input()
print("Prosze podac szerokosc prostokata ")
szerokosc = input()

pole = wysokosc * szerokosc
obwod = 2 * (wysokosc + szerokosc)

print("Pole wynosi {}".format(pole))
print("Obwod wynosi {}".format(obwod))
