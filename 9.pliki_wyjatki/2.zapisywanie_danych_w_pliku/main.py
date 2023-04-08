# ZADANIE 10.3
# GOSC
# Utworz program, który poprosi uzytkownika o podanie imienia, Gdy uzytkownik je wprowadzi, zapisz to imie w pliku o nazwie guest.txt

filename = '9.pliki_wyjatki/2.zapisywanie_danych_w_pliku/guest.txt'

name = input("Podaj swoje imie: ")

with open(filename, 'w') as file:
    file.write(name)


# ZADANIE 10.4
# KSIEGA GOSCI
# Utwörz petle while, w ktorej kazdy uzytkownik bedzie musial podac swoje imie. 
# Gdy uzytkownik je wprowadzi, na ekranie wyswietl komunikat powitania, a do pliku o nazwie guest_book.txt dodaj wiersz rejestrujacy odwiedzenie Twojej strony prez tego uzytkownika. 
# Upewnij sie, ze kardy wpis jest umieszczany w nowym wierszu w pliku.

filename = '9.pliki_wyjatki/2.zapisywanie_danych_w_pliku/guest_book.txt'

print("Podawaj imie gosci, gdy nie bedziesz chcial wiecej napisz 'koniec'")
with open (filename, 'a') as file:
    while True:
        name = input("Podaj imie goscia: ")
        if name == 'koniec':
            break
        else:
            print(f"Witaj {name.title()}!")
            file.write(f"\n{name.title()}")
        
