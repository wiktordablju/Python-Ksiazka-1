"""Zestaw klas ktory bedzie uzywany do zaprezentowania samochodu"""

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