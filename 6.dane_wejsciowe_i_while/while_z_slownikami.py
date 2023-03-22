# EXAMPLES
# -------------------------------------------------------------------------
# unconfirmedUsers = ['alicja', 'bartek', 'katarzyna']
# confirmedUsers = []

# while unconfirmedUsers:
#     current_user = unconfirmedUsers.pop()
    
#     print(f"Weryfikacja uzytkownika {current_user.title()}")
#     confirmedUsers.append(current_user)

# print("\nZweryfikowano nastepujacych uzytkownikow: ")
# for confirmedUser in confirmedUsers:
#     print(confirmedUser.title())

# pets = ['dog', 'cat', 'fish', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# responses = {}

# pollingActive = True

# while pollingActive:
#     name = input("\nPodaj swoje imie: ")
#     response = input("\nNa jaki szczyt chcialbnys sie kiedys wspiac? ")
    
#     responses[name] = response
    
#     repeat = input("Czy ktokolwiek innych chce wziac udzial w ankiecie? (tak/nie)")
    
#     if repeat == 'nie':
#         pollingActive = False
        
# print("\n--- Wyniki ankiety ---")
# for name, response in responses.items():
    # print(f"{name} chcialby sie wspiac na {response}")

# -------------------------------------------------------------------------
# END OF EXAMPLES
    
# ZADANIE 7.8 
# BAR
# Prygotuj liste o nazwie sandwich orders i umiesé na niej nazwy roz-nych kanapek. Nastepnie przygotuj pusta liste o nazwie fintshed_ sandwiches.
# Preprowadz iteracie przez liste zamówionych kanapek i wyswiett informacie o danym zamówieniu, na pryklad: „.Przygotowano kanapke z turezykiem*.
# Kiedy kanaka zostanie robiona, reprezentujacy ja element powinien zostad przeniesiony na liste finished sandwiches. Gdy lista sandwich orders bedzie juz pusta, 
# wyswieti komunikat zawierajacy liste wszystkich zrobionych kanapek.


# ZADANIE 7.9
# BRAK PASTRAMI
# Wykorzystaj liste sandwich orders z ¿wiczenia 7.8 i upew-nij sie, ze na liscie przynajmniej trzykrotnie pojawia sie kanaka z pastrami.
# Gozies na poczatku programu umiest kod wyswietlajacy komunikat, ze w barze skonczyto sie pastrami, a nastepnie za pomoca petli while usun wsystkie wystapienia 
# 'pastrami' z listy sandwich orders. Upewnij sie, ze zadna kanaka z pastrami nie zostanie umieszczona na liscie finished_sandwiches.


# ZADANIE 7.10
# WYMARZONE WAKACJE
# Prygotuj program pytajacy uzytkownikow o ich wymarzone wakacje. Program powinien wyswietlad pytanie w stylu: „Jezeli mogibys odwiedzic jedno dowolne miejsce na 
# swiecie, gdzie bys pojechal?".
# Umiest w programie blok kodu odpowiedzialny za wyswietlenie wyników preprowadzonej ankiety.