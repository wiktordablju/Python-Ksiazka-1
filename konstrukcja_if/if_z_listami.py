# Zadanie 5.8
# WITAJ ADMINISTRATORZE
#Przygotuj liste przynajmniej pieciu nazw uzytkownikow z min. nazwa admin, wyobraz sobie ze to jest kod na powitanie usera po jego zalogowaniu na stronie. Przeprowadz iteracje przez petle
# Jezli nazwa to admin wyswietl specjalne powitanie

# users = ['admin', 'Janeczek', 'Ziolo', 'gigaKOX', 'Steryd3323']
# for user in users:
#     if user == 'admin':
#         print(f"witaj {user}, chcesz zobaczyc raport?")
#     else:
#         print(f"witaj {user}")



# ZADANIE 5.9
# BRAK UZYTKOWWNIKOW
# Przygotowany plik wczesniej dodaj polecenie if ktore spradza czy lista uzytkownikow nie jest pusta

# users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print(f"witaj {user}, chcesz zobaczyc raport?")
#         else:
#             print(f"witaj {user}")
# else:
#     print("Nie ma zadnych ludzi tutaj")



# ZADANIE 5.10
# SPRAWDZANIE NAZW UZYTKOWNIKOW
# Wykonaj ponizsze dzialanie w celu utworzenia programu symulujacego sposob w jaki witryna internetowa gwarantuje ze kazdy uzytkownik bedzie mial unikatowa nazwe
# Utworz liste current users i umiesc 5 nazw
# Utworz liste new users i upewnij sie ze jedna nazwa znajduje sie w current users
# Przeprowadz iteracje przez new users zeby sprawdzic ze nazwa zostala juz wczesniej uzyta, jesli tak wyswietl odpowiedni komunikat
# upewnij sie ze podczas porownywania nazw wielkosc liter nie ma znaczenia

# current_users = ['admin', 'Janeczek', 'Ziolo', 'gigaKOX', 'Steryd3323']
# new_users = ['stEryD3323', 'mulciakson', 'mrozon', 'iceberger']

# current_users_lowercase = []
# new_users_lowercase = []

# for current_user in current_users:
#     current_users_lowercase.append(current_user.lower())
    
# for new_user in new_users:
#     if new_user.lower() in current_users_lowercase:
#         print(f"sorka ale nazwa {new_user} jest juz zajeta")
#     else:
#         print(f"witamy {new_user} na stronie")
        


# ZADANIE 5.11
# LISTY PORZADKOWE
# Liczby porzadkowe wskazuje polozenie elementu na liscie, np 1 2 3. W jezyku angielskim wiekszosc tych liczb konczy sie na th poza 1,2,3
# Utworz liste przechowujaca liczby od 1 do 9
# Przeprowadz iteracje przez liste
# Wykorzystaj if-elif-else wewnatrz petli do prawidlowego wyswietlenia

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# for number in numbers:
#     if number == '1':
#         print(f"{number} to first")
#     elif number == '2':
#         print(f"{number} to second")
#     elif number == '3':
#         print(f"{number} to third")
#     else:
#         print(f"{number} to {number}th")