# ZADANIE 9.4
# LICZBA OBSLUZONYCH
# Prace rozpocznij od programu utworzonego w cwiczeniu 9.1. 
# Dodaj atrybut o nazwie number_ served o wartosci domysinej O.
# Nastepnie na podstawie klasy utworz egzemplarz o nazwie restaurant. 
# Wyswietl liczbe klientow obsluzonych prez restauracje, zmien te wartosc i pozniej wyswietl nowa.
# Dodaj metode o nazwie set_number_served(), pozwalajaca na zdefiniowanie liczby obsluzonych klientow. 
# Wywolaj te metode wraz z róznymi wartosciami i je wyswietl.
# Dodaj metode o nazwie increment _number_served (), pozwalajaca na inkrementacje wartosci wskazujacej a liezbe obstuzonych klientow. 
# Wywolaj te metode dowolna ilosc razy, symulujac w ten sposob liczbe klientow obsluzonych na przyklad w ciagu dnia roboczego.

class Restaurant():
    """Klasa przechowujaca informacje o restauracji"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja danych restauracji"""
        self.name = restaurant_name 
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Wyswietlenie informacji o restauracji"""
        print(f"Restauracja {self.name} specjalizuje sie w kuchni {self.type}")
    
    def open_restaurant(self):
        """Wyswietlanie informacji o godzinach otwarcia restauracji"""
        print(f"Restauracja {self.name} otwarta jest w godzinach 08:00 - 16:00")
        
    def set_number_served(self, customers):
        """Ustala liczbe uzytkownikow obsluzonych w dani dzien"""
        self.number_served = customers
        
    def increment_number_served(self, customers):
        """Zwieksza liczbe obsluzonych uzytkownikow o podana wartosc"""
        self.number_served += customers
        
restaurant = Restaurant('mcdonalds', 'fastfood')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(25)
print(restaurant.number_served)

restaurant.increment_number_served(40)
print(restaurant.number_served)


# ZADANIE 9.5
# PROBY LOGOWANIA
# # Prace rozpocznij od programu utworzonego w cwiczeniu 9.3. 
# Do klasy User dodaj metode o nazwie increment_login_attempts (), pozwalajacy na inkrementacje wartosci login_attempts o 1. 
# Utworz druga metode o nazwie reset_login_attempts (), ktöra bedzie zerowala wartosc login attempts.
# Utwörz egzemplarz klasy User i kilkukrotnie wywolaj metode increment login attempts (). 
# Wyswietl wartosc login attempts, aby miec pewnosc o jej prawidowej inkrementacji. 
# Nastepnie wywotaj metode reset_login_attempts ().
# Ponownie wyswietl wartost login attempts i sprawdz, czy na pewno wynosi 0.

class User():
    """Klasa przechowujaca informacje o uzytkowniku"""
    def __init__(self, name, surname, nickname, age, sex):
        """Inicjalizuje informacje o uzytkowniku"""
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.age = age
        self.sex = sex
        self.login_attempts = 0
    
    def describe_user(self):
        """Opisuje profil uzytkownika"""
        print(f"\nOto informacje o użytkowniku {self.name} {self.surname}:")
        print(f"Pseudonim - {self.nickname}")
        print(f"Wiek - {self.age}")
        print(f"Plec - {self.sex}")
        
    def greet_user(self):
        """Wita uzytkownika jego atrybutami"""
        print(f"\nHej {self.nickname}, jak leci?")
    
    def increment_login_attempts(self):
        """Zwieksza ilosc niepoprawnych prob zalogowania sie o 1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Resetuje wartosc nieudanych prob zalogowania sie"""
        self.login_attempts = 0

user = User('wiktor', 'dziendziel', 'dablju', '18', 'mezczyzna')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(user.login_attempts)

user.reset_login_attempts()

print(user.login_attempts)