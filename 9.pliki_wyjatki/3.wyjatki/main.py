# ZADANIE 10.6
# DODAWANIE
# Jeden z najczesciej pojawiajacych sie problemów podczas pobierania danych liczbowych polega na tym, ze uzytkownicy podaja tekst zamiast liczb. 
# Kiedy tego rodzaju dane wejsciowe sprobujesz skonwertowac na typ int, otrzymasz blad ValueError. 
# Utwörz program, który prosi uzytkownika o podanie dwoch liczb. 
# Dodaj je i wyswietl wynik. 
# Przechwyc blad ValueError, jezeli ktorakolwiek wartosc przekazana w danych wejsciowych nie jest liczba, i wyswietl odpowiedni komunikat bledu. 
# Prztestuj program, najpierw podajac dwie liczby, a pozniej pewien tekst zamiast liczby.
# Kod opakuj petla while, aby uzytkownik mogl kontynuowac wprowadzanie liczb nawet po popeinieniu bledu i podaniu tekstu zamiast liczby.

while True:
    print("\nPodaj dwie liczby a ja je dodam")
    print("Aby wyjsc napisz 'q'")
    try:
        first_number = input("Pierwsza liczba: ")
        if first_number == 'q':
            break
        second_number = input("Druga liczba: ")
        if second_number == 'q':
            break
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Nie podano liczb")
    else:
        print(f"{first_number} dodać {second_number} wynosi: {answer}")


# ZADANIE 10.8
# KOTY I PSY
# Utwörz dwa pliki o nazwach cats.txt i dogs.txt. 
# W pierwszym pliku umiesé przynajmniej try imiona kotów, natomiast w drugim przynajmniej try imiona psów. 
# Przygotuj program próbujacy odczytac zawartosc tych plikow i wyswietlic ja na ekranie. 
# Zastosuj w kodzie konstrukcje try-except, aby przechwycic wszelkie bledy typu FileNotFoundError i wyswietlic uzytkownikowi odpowiedni komunikat bledu, gdy podany plik nie istnieje. 
# Jeden z utworzonych wczesniej plikow przenies do innego katalogu w systemie i upewnij sie, ze opracowany blok except w programie dziala prawidlowo.
# Blok except w programie zmodyfikuj w taki sposob, aby brak pliku powodowal jedynie ciche niepowodzenie.

dogs_file = '9.pliki_wyjatki/3.wyjatki/dogssssss.txt'
cats_file = '9.pliki_wyjatki/3.wyjatki/cats.txt'

try:
    with open(dogs_file, 'r', encoding='utf-8') as dogs:
        content = dogs.read()
except FileNotFoundError:
    pass
else:
    print("\nZawartość pliku dogs.txt: ")
    print(content)
   
try: 
    with open(cats_file, 'r', encoding='utf-8') as cats:
        content = cats.read()
except FileNotFoundError:
    pass
else:
    print("\nZawartośc pliku cats.txt: ")
    print(content)
    
    