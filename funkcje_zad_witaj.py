# coding: utf-8

# Ukąś Pythona 4


#Zadanie z imieniem -> Witaj (5min - 12min)


print " \n ------------- Zadanie z imieniem -> Witaj  ----------------- \n "

print " \n Sposob1 ----------- "
# #definicja
# def ask(param = None):
#     if param is None:  # Porównanie czegoś z 'None' zawsze przez 'is'
#         param = input('podaj imię: ')
#     else:
#         print 'Witaj', param
# # wywołanie
# ask()

print " \n Sposob1 ale inny zapis w 1 linijce  ----------- "
# def ask(param = None):
#     print 'witaj', param or input('Podaj imię: ')
#
# ask()

print " \n Sposob2 ----------- "
# def ask(param = ''):
#     if param == '':  ## Porównania czegos z czyms możemy normalnie '=='
#         param = input('podaj imię: ')
#     print 'Witaj', param
#
# ask()

print " \n ------------- Różne zapisy Idiomy w 1 linii  ----------------- \n "
x = int(input('Podaj liczbę: '))
y = 42 if x > 0 else -1  # Przypisz dla 'y' wartość 42 jeśli 'x' > 0 w przeciewnym wypadku przypisz -1
print y



