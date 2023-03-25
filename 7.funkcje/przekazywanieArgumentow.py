# ZADANIE 8.3
# T-SHIRT
#  Utworz funkcje o nazwie makeshirt(), akceptujaca wielkosc koszulki oraz tekst, ktory ma zostac na niej nadrukowany. Funkcja powinna wyswietlic zdanie zawierajace informacje dotyczace zamówionej koszulki: jej rozmiar i tekst do wydrukowania na niej.
# W trakcie pierwszego wywolania funkcji do przygotowania koszulki zastosuj argumenty pozycyne. Natomiast w trakcie drugiego wywolania uzyj argumentów w postaci slów kluczowych.

def makeShirt(size, text):
    """Wyswietla tworzenie koszulki o podanym rozmiarze i tekscie"""
    print(f'Zamówiono koszulkę o rozmiarze {size} oraz nadrukiem "{text}" ')

makeShirt('XL', 'WIEZA HANOI')
makeShirt(size='L', text='Ja ogolnie to lubie programowac')


# ZADANIE 8.4
# DUZE KOSZULKI
# Zmodyfikuj funkcje makeshirt() tak, aby domysinie byty przygotowywane duze koszulki z nadrukowanym tekstem „Uwielbiam Pythona".
# Utwörz koszulki w rozmiarze duzym i Srednim (obie z domyslnym tekstem) oraz koszulke w dowolnym rozmiarze i z innym tekstem nadrukowanym na niej.

def makeShirt(size, text='Uwielbiam Pythona'):
    """Wyswietla tworzenie koszulki o podanym rozmiarze i tekscie"""
    print(f'Zamówiono koszulkę o rozmiarze {size} oraz nadrukiem "{text}" ')

makeShirt('XL')
makeShirt(size='L')
makeShirt(size='S', text='Ja ogolnie to lubie programowac')


# ZADANIE 8.5
# MIASTA
# Utworz funkcje o nazwie describe_city(), akceptujaca nazwe miasta i kraju. 
# Ta funkcja powinna wyswietlac proste dane, takie jak „Warszawa lezy w Polsce". 
# Parametrowi prechowujacemu nazwe pañstwa przypisz wartosé domyslna. 
# Przygotowana funkcje wywolaj dla trzech róznych miast, z ktorych prynajmniej jedno nie powinno by polozone w domysinie zdefiniowanym kraju.

def describeCity(name, country='polska'):
    """Wyswietla informacje na temat podanego miasta"""
    print(f"{name.title()} leży w {country.title()}")

describeCity('katowice')
describeCity(name='WarRSzawa')
describeCity(name='seul', country='korea poludniowa')