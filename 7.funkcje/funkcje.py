# ZADANIE 8.1
# KOMUNIKAT
# Utworz funkcje o nazwie display_messages () wyswietlajaca jedno zdanie informujace o tym, czego sie uczysz w tym rozdziale. Wywolaj przygotowana funkcje i upewnij sie, ze komunikat zostal prawidLowo wyswietlony.

def displayMessages():
    """Wyświetla jakich informacji naucze się w tym rozdziale"""
    print("W tym rozdziale naucze sie tego jak dzialaja funkcje w pythonie")

displayMessages()


# ZADANIE 8.2
# ULUBIONA KSIAZKA
# Utworz funkcje o nazwie favoritebook(), która akceptuje jeden parametr title. Ta funkcja powinna wyswietlac komunikat w stylu:
# „Jedna z moich ulubionych ksiazek jest Alicja w krainie czarów". Wywolaj te funkcje i upewnij sie, ze podales tytul ksiazki jako argument.

def favouriteBook(title):
    print(f"Jedna z moich ulubionych ksiazek to: {title.title()}")
    
favouriteBook('dziady cz.3')