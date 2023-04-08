import json

# numbers = [2, 3, 4, 5]

# filename = '9.pliki_wyjatki/4.przechowywanie_danych/numbers.json'

# with open(filename, 'w') as f:
#     json.dump(numbers, f)
    
# filename = '9.pliki_wyjatki/4.przechowywanie_danych/numbers.json'

# with open(filename) as f:
#     numbers = json.load(f)

# print(numbers)


import json

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
        print(f"Witaj ponownie, {username}!")
    else:
        username = get_new_username()
        print(f"Bedziemy cie pamietac jak wrocisz, {username}!")

greet_user()