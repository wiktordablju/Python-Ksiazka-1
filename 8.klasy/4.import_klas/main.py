from car import Car, ElectricCar
# import car

my_new_car = Car('tesla', 'model s', 2019)
# my_new_car = car.Car('tesla', 'model s', 2019) taki zapis w przypadku sotowania po prostu import

print(my_new_car.get_descriptive_name())

my_new_tesla = ElectricCar('tesla', 'model x', 2022)
my_new_tesla.battery.describe_battery()