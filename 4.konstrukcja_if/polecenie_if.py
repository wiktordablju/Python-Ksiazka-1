#ZADANIE 5.3
#KOLORY OBCYCH CZESC 1
#Wyobraz sobie zestrzelenie obcego w grze
#Utworz zmienna o nazwie alien_color i przypisz jej wartosci zielony zolty lub czerwony
#Przygotuj polecenie if sprawdzajace czy kolorem obcego jest zielony, jesli tak to wyswietl ze zarobil 5 punktow, oraz jesli nie komunikat o niepowodzeniu

# alien_color = 'czerwony'
# if alien_color == 'zielony':
#     print("Zarobiłeś 5pkt")
# else:
#     print("Nie udało się zestrzelić zielonego obcego")


#ZADANIE 5.4
#KOLORY OBCYCH CZESC 2
#Podobnie jak w 5.3, wybierz kolor obcego a nastepnie stworz if-else
#Jezeli kolor obcego to zielony, wyswietl komunikat ze zarobil 5 pkt
#Jezeli kolor jest inny niz zielony to wyswietl ze zarobil 10 punktow

# alien_color = 'czerwony'
# if alien_color == 'zielony':
#     print("Zarobiłeś 5pkt")
# else:
#     print("Zarobiles 10pkt")


#ZADANIE 5.5
#KOLORY OBCYCH CZESC 3
#5.4 zastap if-elif-else
#Jesli zielony - 5pkt
#Jesli zolty - 10pkt
#Jesli czerwony - 15pkt

# alien_color = 'czerwony'
# if alien_color == 'zielony':
#     print("Zarobiłeś 5pkt")
# elif alien_color == 'zolty':
#     print("Zarobiles 10pkt")
# elif alien_color == 'czerwony':
#     print("Zarobiles 15pkt")


#ZADANIE 5.6
#ETAPY ZYCIA
#Przygotuj if-else ustalajaca etap zycia danej osoby, Przypisz wartosc ziennej age a nastepnie
#jesli mniej niz 2 lata wyswietl ze jest niemowlakiem
#Jesli conajmniej 2 ale mniej niz 4 - dzieckiem ktore sie uczy chodzic
#Jesli conajmniej 4 ale mniej niz 13 - dziecko
#Jesli conajmniej 13 ale mniej niz 20 - nastolatek
#Jesli conajmniej 20 a mniej niz 65 - dorosly
#Jesli conajmniej 65 - senior\
    
# age = 15
# if age > 65:
#     print("Senior")
# if age > 20 and age < 65:
#     print("Dorosly")
# if age > 13 and age < 20:
#     print("Nastolatek")
# if age > 4 and age < 13:
#     print("Dziecko")
# if age > 2 and age < 4:
#     print("Dziecko uczace sie chodzic")
# if age < 2:
#     print("Niemowlak")


#ZADANIE 5.7
#ULUBIONE OWOCE
#Przgotuj liste ulubonych owocow a nastepnie utworz serie niezaleznych polecen if sprawdzajacych obecnosc okreslonych owocow na liscie
# fruits = ['banan', 'kiwi', 'grejpfrut']
# if 'banan' in fruits:
#     print("Naprawde lubisz banany")
# if 'jablko' in fruits:
#     print("Naprawde lubisz jablka")
# if 'kiwi' in fruits:
#     print("Naprawde lubisz kiwi")