# ZADANIE 8.15
# WYDRUK MODELI
# Funkcje z programu print models.py umiesc w oddzielnym pliku o nazwie printing_functions.py Na poczatku pliku print_models.py umiesc polecenie import i zmodyfikuj plik w taki sposob, aby uzywac zaimportowanych funkcji.
# Uzylem innego pliku

from build_car_info import buildCarInfo as buildCar

newCar = buildCar('mercedes', 's-class', color='black', additionalEquipement = 'none')

print(newCar)

