# ZADANIE 7.8 
# BAR
# Prygotuj liste o nazwie sandwich orders i umiesé na niej nazwy roz-nych kanapek. Nastepnie przygotuj pusta liste o nazwie fintshed_ sandwiches.
# Preprowadz iteracie przez liste zamówionych kanapek i wyswiett informacie o danym zamówieniu, na pryklad: „.Przygotowano kanapke z turezykiem*.
# Kiedy kanaka zostanie robiona, reprezentujacy ja element powinien zostad przeniesiony na liste finished sandwiches. Gdy lista sandwich orders bedzie juz pusta, 
# wyswieti komunikat zawierajacy liste wszystkich zrobionych kanapek.

sandwich_orders = ['klasyczna', 'szynka', 'wege']
finished_sandwiches = []

active = True
while active:
    for sandwich_order in sandwich_orders:
        print(f"Przygotowano kanapkę: {sandwich_order}")
        sandwich_orders.pop()
        finished_sandwiches.append(sandwich_order)
        
        if sandwich_orders == []:
            active = False
            print("Zakończono robienie wszystkich kanapek")

print(f"Przygotowano kanapki z: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


# ZADANIE 7.9
# BRAK PASTRAMI
# Wykorzystaj liste sandwich orders z ¿wiczenia 7.8 i upew-nij sie, ze na liscie przynajmniej trzykrotnie pojawia sie kanaka z pastrami.
# Gozies na poczatku programu umiest kod wyswietlajacy komunikat, ze w barze skonczyto sie pastrami, a nastepnie za pomoca petli while usun wsystkie wystapienia 
# 'pastrami' z listy sandwich orders. Upewnij sie, ze zadna kanaka z pastrami nie zostanie umieszczona na liscie finished_sandwiches.

sandwich_orders = ['pastrami', 'klasyczna', 'szynka', 'pastrami', 'wege', 'pastrami']
finished_sandwiches = []

print("Skończyło nam się pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

active = True
while active:
    for sandwich_order in sandwich_orders:
        print(f"Przygotowano kanapkę: {sandwich_order}")
        sandwich_orders.pop()
        finished_sandwiches.append(sandwich_order)
        
        if sandwich_orders == []:
            active = False
            print("Zakończono robienie wszystkich kanapek")

print(f"Przygotowano kanapki z: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


# ZADANIE 7.10
# WYMARZONE WAKACJE
# Prygotuj program pytajacy uzytkownikow o ich wymarzone wakacje. Program powinien wyswietlad pytanie w stylu: „Jezeli mogibys odwiedzic jedno dowolne miejsce na 
# swiecie, gdzie bys pojechal?".
# Umiest w programie blok kodu odpowiedzialny za wyswietlenie wyników preprowadzonej ankiety.

responses = {}

active = True


while active:
    name = input("Jak masz na imie? ")
    response = input(f"Dobrze {name}, gdzie chciałbys pojechać na wakacje ")
    responses[name] = response
    
    repeat = input("\nCzy ktoś jeszcze chce wziąc udział w ankiecie? (tak/nie) ")
    if repeat == 'nie':
        active = False
    
print("\nWYNIKI ANKIETY:")
for name, response in responses.items():
    print(f"{name.title()} chce spędzić wakacje w {response.title()}")
    