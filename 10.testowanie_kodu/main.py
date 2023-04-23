
# ZADANIE 11.1
# MIASTO, PANSTWO
# Przygotuj funkcje akceptujaca dwa parametry: nazwy miasta i panstwa. 
# Wartoscia zwrotna tej funkcji powinien byc pojdynczy ciag tekstowy w postaci Miasto, Pañstwo, na przyklad Santiago, Chile. 
# Gotowa funkcje umiest w module o nazwie city_functions.py
# Utworz plik o nazwie test_cities.py przeznaczony do przetestowania przygotowanej wczesniej funkcji (pamietaj o koniecznosci zaimportowania modulu unittest oraz funkcji, która ma zostad sprawdzona). 
# Nastepnie w pliku test_cities py zdefiniuj funkcje o nazwie test _city_country() odpowiedzialna za sprawdzenie, czy wywotanie utworzonej w poprzednim cwiczeniu funkeji, na przyklad z wartosciami 'santiago' i 'chile', spowoduje wygenerowanie oczekiwanego ciagu tekstowego. Uruchom plik test _cities.py i upewnij sie, ze test test_city_country () zostaje zaliczony.

# ZADANIE 11.2
# POPULACJA
# Zmodyfikuj prygotowana wezesniej funkcje, aby wymagala podania trzeciego argumentu - populacji (population). 
# Teraz wartoscia zwrotna funkcji powinien by ciag tekstowy w postaci Miasto, Pañstwo - populacja xxx, na przyklad Santiago, Chile - populacja 5000000. 
# Ponownie uruchom test_cities.py. Upewnij sie, ze tym razem test zdefiniowany w metodzie test_city_country () bedzie niezaliczony.
# Zmodyfikuj funkcje, aby parametr population byl opcjonalny. Ponownie uruchom test _cities.py i upewnij sie, ze rowniez teraz test zdefiniowany w metodzie test_city_country () zostanie zaliczony.
# Utwörz drugi test o nazwie test _city country_population (), sprawdzajacy, czy mozna wywolad funkcje z wartosciami 'santiago', 'chile' i 'population +=5000000'. Raz jeszcze uruchom test_cities.py i upewni sie, ze nowy test zostal zaliczony.


def city_country(city, country, population=''):
    if population:
        city_country_info = f"{city}, {country} - populacja {population}"
    else:
        city_country_info = f"{city}, {country}"
    return city_country_info.title()



# ZADANIE 11.3
# PRACOWNIK
# Przygotuj klase o nazwie Employee. 
# Metoda _init ( powinna pobieraC imie, nazwisko i roczne wynagrodzenie, a nastepnie zapisac te informacje w postaci atrybutow. 
# Utworz metode o nazwie give.raise(), która spowoduje zwiekszenie wynagrodzenia domsylnie o 5000 zl. 
# choc zaakceptuje take inna kwote.
# Przygotuj zestaw testów dla Klasy Employee. 
# Utworz dwie metody testowe test give_default_raise) i test_give_custom_raise(). 
# Wykorzystaj metode setUp(), aby uniknac koniecznosci tworzenia nowego egzemplarza klasy Employee w kazdej metodzie testowej. 
# Wykonaj zestaw testów i upewnij sie, ze oba testy zostana zaliczone.

class Employee():
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        
    def give_raise(self, amount = 5000):
        self.salary += amount
        
    def show_employee(self):
        return f"Imie - {self.name}\nNazwisko - {self.surname}\nZarobki - {self.salary}"
