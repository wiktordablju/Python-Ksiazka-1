# ZADANIE 10.1
# POZNAJEMY PYTHONA
#  W edytorze tekstu utwórz pusty plik i wpisz w nim kilka danych podsumowujacych to, czego sie dotad nauczytes o jezyku Python.
# Kazdy wiersz rozpocznij od wyrazenia „W Pythonie mozna...". 
# Plik zapisz pod nazwa learning_python.txt w tym samym katalogu, w którym umieszczasz cwiczenia z tego rozdzialu. 
# Przygotuj program odczytujacy powyzszy plik i trzykrotnie wyswietlajacy jego zawartosc. Tresc pliku powinna by wyswietlona raz przez odczytanie calego pliku, raz za pomoca iteracji przez obiekt pliku oraz raz prez umieszczenie wierszy na liscie, a nastepnie przetworzenie listy poza blokiem with

filename = '9.pliki_wyjatki/1.odczytanie_danych_z_pliku/learning_python.txt'

with open(filename) as file:
    print(f"Wyswietlona za pomoca for: \n")
    for line in file:
        print(line.strip())

with open(filename) as file:
    contents = file.read()

print(f"\nWyswietlone za pomoca read(): \n{contents}")

with open(filename) as file:
    lines = file.readlines()
    print(f"\nWyswietlone za pomoca readlines(): \n")
    for line in lines:
        print(line.strip())


# ZADANIE 10.2
# POZNAJEMY C
# Metode replace () mozna wykorzystac do zastapienia dowolnego slowa w ciagu tekstowym zupenie innym slowem. 
# Oto krötki przykklad pokazujacy, jak w zdaniu slowo pies zastapic stowem kot:
# message = "Moje ulubione zwierze to pies."
# message. replace ('pies', 'kot')
# "Moje ulubione zwierze to kot."
# Odczytaj kazdy wiersz tekstu w utworzonym wezesniej pliku learning_python.text, a nastepnie wszystkie wystapienia slowa Python zastap nazwa innego jezyka programowania, na przyklad C. Kazdy zmodyfikowany wiersz wyswietl

filename = '9.pliki_wyjatki/1.odczytanie_danych_z_pliku/learning_python.txt'

messages = ''

with open(filename) as file:
    for line in file:
        messages += line
        
print(messages.replace('pythonie', 'C'))


