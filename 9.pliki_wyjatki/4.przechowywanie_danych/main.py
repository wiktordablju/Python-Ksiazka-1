import json
# ZADANIE 10.x
# UZYTKOWNIK I WERYFIKACJA
# Przechowuj nazwe uzytkownika w pliku json, sprawdz czy jest juz jakies imie w nim, jesli nie to wpisz nowo podane do niego. Na poczatku programu zapytaj czy wczytanie z pliku imie jest poprawne

def get_stored_username():
    """Pobieranie imienia z pliku, jesli istnieje"""
    filename = '9.pliki_wyjatki/4.przechowywanie_danych/user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Poproszenie uzytkowniak aby podal swoje imie a nastepnie zapisanie tego imienia w pliku"""
    username = input("Jak sie nazywasz? ")
    filename = '9.pliki_wyjatki/4.przechowywanie_danych/user.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Przywitanie uzytkownika z uzyciem jego imienia"""
    username = get_stored_username()
    if username:
        print(f"Ostatnio zalogowany uzytkownik to: {username}")
        is_username_good = input("Czy imie ostatniego uzytkownika jest poprawne? (Tak/Nie): ")
        if is_username_good.lower() == 'tak':
            print(f"Witaj ponownie, {username}!")
        else:
            username = get_new_username()
            print(f"Bedziemy cie pamietac jak wrocisz, {username}!")
    else:
        username = get_new_username()
        print(f"Bedziemy cie pamietac jak wrocisz, {username}!")

greet_user()
 

