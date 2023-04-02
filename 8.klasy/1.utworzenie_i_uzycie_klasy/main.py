# ZADANIE 9.1
# RESTAURACJA
# Przygotuj klase o nazwie Restaurant. Metoda init (w klasie Restaurant powinna prechowywac dwa atrybuty: restaurant_name i cuisine_type). 
# Utwörz metode o nazwie describe restaurant () wyswietlajaca te dwa fragmenty informacji oraz metode o nazwie open_restaurant () wyswietlajaca informacje o godzinach pracy restauracji.
# Na podstawie przygotowanej klasy utworz egzemplarz restaurant. 
# Wyswietl oddzielnie oba atrybuty, a nastepnie wywolaj obie metody.

class Restaurant():
    """Klasa przechowujaca informacje o restauracji"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja danych restauracji"""
        self.name = restaurant_name 
        self.type = cuisine_type
        
    def describe_restaurant(self):
        """Wyswietlenie informacji o restauracji"""
        print(f"Restauracja {self.name} specjalizuje sie w kuchni {self.type}")
    
    def open_restaurant(self):
        """Wyswietlanie informacji o godzinach otwarcia restauracji"""
        print(f"Restauracja {self.name} otwarta jest w godzinach 08:00 - 16:00")
        
McDonalds = Restaurant('McDonalds', 'Fastfood')
print(McDonalds.name)
print(McDonalds.type)
McDonalds.describe_restaurant()
McDonalds.open_restaurant()
        

# ZADANIE 9.2
# TRZY RESTAURACJE
#  Prace rozpocznij od klasy opracowanej w ¿wiczeniu 9.1.
# Utworz trzy rózne egzemplarze na podstawie tej klasy, a nastepnie wywolaj metode describe restaurant () da kazdego egemplarza.

pizza_hut = Restaurant('PizzaHut', 'Pizza')
starbucks = Restaurant('Starbucks', 'Kawa')

pizza_hut.describe_restaurant()
starbucks.describe_restaurant()


# ZADANIE 9.3
# UZYTKOWNICY
# Przygotuj klase o nazwie User. 
# Zdefiniuj w niej dwa atrybuty (first name i last _name), a nastepnie utworz kilka innych atrybutow, które zwykle sa przechowywane w profilu uzytkownika. 
# Zdefiniuj metode o nazwie describe user (), wyswietlajaca podsumowanie informacji zebranych o uzytkowniku. 
# Utwörz jeszcze druga metode o nazwie greet user (), ktora bedzie wyswietlala uzytkownikowi spersonalizowane powitanie
# Utworz kilka egzemplarzy reprezentujacych róznych uzytkowników, a nastepnie dla kazdego z nich wywolaj obie metody.

class User():
    """Klasa przechowujaca informacje o uzytkowniku"""
    def __init__(self, name, surname, nickname, age, sex):
        """Inicjalizuje informacje o uzytkowniku"""
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        """Opisuje profil uzytkownika"""
        print(f"\nOto informacje o użytkowniku {self.name} {self.surname}:")
        print(f"Pseudonim - {self.nickname}")
        print(f"Wiek - {self.age}")
        print(f"Plec - {self.sex}")
        
    def greet_user(self):
        """Wita uzytkownika jego atrybutami"""
        print(f"\nHej {self.nickname}, jak leci?")
        
dablju = User('Wiktor', 'Dziendziel', 'dablju', 18, 'Mezczyzna')
mrozon = User('Kamil', 'Mrowiec', 'Mrozon', 18, 'Mezczyzna')
ziolo = User('Oliwier', 'Kotlicki', 'ziolo', 17, 'Mezczyzna')

ziolo.describe_user()
ziolo.greet_user()

dablju.describe_user()
dablju.greet_user()

mrozon.describe_user()
mrozon.greet_user()