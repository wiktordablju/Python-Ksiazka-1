# ZADANIE 8.12
# KANAPKI
# Utwörz funkcje akceptujaca liste skladnikow, które klient chce umiescic w zamawianej kanapce. 
# Funkcja powinna zawieraC jeden parametr przechowujacy dowolna liczbe argumentow przekazanych w wywolaniu funkcji oraz wyswietlac podsumowanie dotyczace zamówionej kanapki. 
# Przygotowana funkcje wywolaj trzykrotnie, za kazdym razem z inna liezba argumentów.

def showOrderedToppings(*orderedToppings):
    """Wyswietla informacje o zamowionej kanapce przez klienta"""
    print("\nKanapka zostala zamowiona z nastepujacymi skladnikami")
    for orderedTopping in orderedToppings:
        print(f"- {orderedTopping}")

showOrderedToppings('ser')
showOrderedToppings('ser', 'szynka')
showOrderedToppings('ser', 'sos pomidorowy', 'ananas', 'banan', 'swiezy kakaowiec')


# ZADANIE 8.13
# PROFIL UZYTKOWNIKA
# Prace rozpocznij od kopii programu user_profile.py utworzonego nieco weczesniej w tym rozdziale. 
# Przygotuj wlasny profil przez wywolanie funkcji build profile (), podaj imie, nazwisko oraz trzy inne pary klucz-wartosc, ktore Cie opisuja.

def buildProfile(name, surname, **userInfo):
    """Tworzy slownik z informacjami o uzytkowniku"""
    userInfo['name'] = name
    userInfo['surname'] = surname
    return userInfo

wiktorProfile = buildProfile('wiktor', 'dziendziel', location='katowice', field='it', sex='male', status='student')
print(wiktorProfile)


# ZADANIE 8.14
# SAMOCHODY
# Utwórz funkcje prZechowujaca w slowniku informacje o samochodzie. 
# Ta funkcja zawsze powinna otrzymywac nazwy marki i modelu pojazdu, po którym mozna podac dowolna liczbe argumentów w postaci slow kluczowych. 
# Wywolaj funkcje zawierajaca wymagane informacje oraz dwie dodatkowe pary nazwa-wartosc, na przyklad opisujace kolor i wyposazenie dodatkowe. 
# Przygotowana funkcja powinna byc wywolywana w sposób podobny do przedstawionego ponizej:
# car = make _car('subaru', 'outback', colors'blue', tow_package=True)
# Wyswietl zawartosc słownika zwroconego przez te funkcje i upewnij sie, ze wszystkie podane informacje zostaly w nim prawdilowo zapisane.

def buildCarInfo(brand, model, **carInfo):
    """Tworzy slownik z informacjami o samochodzie"""
    carInfo['brand'] = brand
    carInfo['model'] = model
    return carInfo

newCar = buildCarInfo('mercedes', 's-class', color='black', additionalEquipement = 'none')

print(newCar)