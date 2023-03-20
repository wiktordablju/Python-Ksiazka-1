# ZADANIE 7.1
# WYPOZYCZENIE SAMOCHODU
# Zapytaj jakiej marki samochod chcialby wypozyczyc, nastepnie wyswietl komunikat ze sprawdzimy czy ten samochod jets dostepny

message = "Jakiej marki samochód chciałby pan wypożyczyć? "
requestedCar = input(message)
print(f"Sprawdzę czy samochód marki {requestedCar} jest dostępny")


# ZADANIE 7.2
# STOLIK W RESTAURACJI
# Utworz program pytajacy klienta na ile osob chce zarezerwowac stolik, jesli licza jest wieksza niz 8 wyswietl ze musi poczekac na stolik

message = "Na ile osób chciałby Pan/Pani zarezerwować stolik? "
requestedSize = input(message)
requestedSize = int(requestedSize)
if requestedSize > 8:
    print("Proszę poczekać na stolik")
else:
    print("Zapraszam do stolika")


# ZADANIE 7.3
# WIELKROTNOSC DZIESIECIU
# Popros o podanie dowolnej liczby a nastepnie sprawdz czy jest wielkrotnoscia 10

message = "Proszę podaj jakąś liczbę a ja sprawdzę czy jest wielokrotnością 10 " 
number = input(message)
number = int(number)
if number % 10 == 0:
    print(f"Liczba {number} jest wielokrotnościa 10")
else:
    print(f"Liczba {number} nie jest wielokrotnością 10 ")