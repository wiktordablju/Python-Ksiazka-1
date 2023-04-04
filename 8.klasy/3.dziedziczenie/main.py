# ZADANIE 9.6
# BUDKA Z LODAMI
# Budka z lodami to szczegoiny rodzaj restauracji. 
# Zdefiniuj klase o nazwie IceCreamstand dziedziczaca po klasie Restaurant utworzonej w cwiczeniu 9.1 lub 9.4; 
# Dodaj atrybut o nazwie Savors, przechowujacy liste röznych smakow lodow. 
# Zdefiniuj metode wyswietlajaca dostepne smaki lodow. 
# Utwörz egzemplarz klasy IceCreamStand i wywolaj nowa metode.

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


class IceCreamStand(Restaurant):
    """Klasa przechowujaca informacje o specjalnej instancji restauracji, stoisku z lodami"""
    def __init__(self, restaurant_name, cuisine_type, savorsList = []):
        super().__init__(restaurant_name, cuisine_type)
        self.savorsList = savorsList
        
    def availableSavors(self):
        print("\nDostępne smaki lodów: ")
        for savor in self.savorsList:
            print(f"- {savor}")

            
zielona_dolina = IceCreamStand('Zielona Dolina', 'Lody', ['czekolada', 'smietana', 'mieta'])
zielona_dolina.availableSavors()
            
            
# ZADANIE 9.7
# ADMIN
# Administrator to specjalny rodzaj uzytkownika. 
# Zdefiniuj klase o nazwie Admin dziedziczaca po Klasie User utworzonej w cwiczeniu 9.3 lub 9.5.
# Dodaj atrybut privileges przechowujacy liste ciagow tekstowych takich jak „moze dodac post", «moze usunac post" czy moze zbanowac uzytkownika" zdefiniuj metode o nazwie show_ privileges (), wyswietlajaca liste uprawnien administratora. 
# Utworz egzemplarz klasy Admin i wywolaj nowa metode.

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

class Admin(User):
    """Specjalna instancja dla administrator"""
    def __init__(self, name, surname, nickname, age, sex):
        super().__init__(name, surname, nickname, age, sex)
        self.privileges = ['moze dodawac posty', 'moze zbanowac uzytkownika']
    
    def show_privileges(self):
        print("\nMozliwosci admina: ")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
dablju = Admin('wiktor', 'dziendziel', 'dablju', '18', 'mezczyzna')
dablju.show_privileges()


# ZADANIE 9.8
# UPRAWNIENIA
# Zdefinij oddzielna klase Privileges. 
# Ta klasa powinna miec jeden atrybut (privileges), przechowujacy liste ciagów tekstowych, tak jak przedstawi;em to w poprzednim cwiczeniu. 
# Metode show privileges () przenies do nowej klasy. 
# Utwörz egzemplarz klasy Privileges jako atrybut w klasie Admin. 
# Nastepnie utworz nowy egzemplarz klasy Admin i uzyj metody show privileges () do wyswietlenia uprawnien.

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

            
class Privileges():
    """Klasa na uprawnienia administratora"""
    def __init__(self):
        self.privileges = ['moze dodawac posty', 'moze zbanowac uzytkownika']
        
    def show_privileges(self):
        print("\nMozliwosci admina: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Specjalna instancja dla administrator"""
    def __init__(self, name, surname, nickname, age, sex):
        super().__init__(name, surname, nickname, age, sex)
    privilege = Privileges()

dablju = Admin('wiktor', 'dziendziel', 'dablju', '18', 'mezczyzna')
dablju.privilege.show_privileges()


# ZADANIE 9.9
# UAKTUALNIENIE AKUMULATORA
# Prace rozpocznij od ostatniej wersji programu electric_car.py utworzonej w tym podrozdziale. 
# Do klasy Battery dodaj nowa metode o nazwie upgrade_battery (). 
# Ta metoda powinna sprawdzic pojemnosc akumulatora i ustawic ja na 100, jesli aktualnie jest inna. 
# Utwor egzemplarz samochodu o napedzie elektrycznym wraz z akumulatorem o domyslnej pojemnosci, wywolaj metode get_range (), a nastepnie metode upgrade_battery() i ponownie get_range (). 
# Powinienes zauwazyc zwiekszenie zasiegu samochodu.

class Car():
    """Prosta proba zaprezentowania samochodu"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_game =f"{self.year} {self.make} {self.model}"
        return long_game.title()
    
    def read_odometer(self):
        print(f"Ten samochod przejechal {self.odometer_reading} km")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("nie mozna cofnac licznika")
    
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers
    
class ElectricCar(Car):
    """Cechy charakterystyczne dla samochodu elektrycznego """
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzednej"""
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery():
    """Wyswietla ifnormacje o baterii"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Wyswietlenie informacji na temat bateri"""
        print(f"ten samochod ma akumulator o pojemnosci {self.battery_size} kWh")
        
    def get_range(self):
        """Wyswietla obecny zasieg akumulatora"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"Przy obecnym naladowaniu zasieg wynosi: {range}")

    def upgrade_battery(self):
        """Ulepsza baterie samochodu uzytkownika"""
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print(f"Twoj akumulator nie moze byc ulepszony, obecnie prowadzimy program ulepszania baterii do 100kWh a twoj samochod ma {self.battery_size}")



my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()


