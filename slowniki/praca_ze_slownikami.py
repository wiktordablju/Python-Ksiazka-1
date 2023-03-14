# ZADANIE 6.1
# OSOBA
# Wykorzystaj slownik do przechowania informacji o znanej ci osobie.
# W slowniku powinny znalezc sie informacje takie jak imie nazwisko wiek i miasto

person = {
    'name':  'kamil',
    'surname': 'mrowiec',
    'age': 18,
    'city': 'siemianowice slaskie',
}


# ZADANIE 6.2
# ULBIONE LICZBY
# Wykorzystaj slownik do przechowania ulubionych liczb roznych osob
# Wez pod uwage 5 osob i uzyj ich imion 

numbers = {
    'kamil': 14,
    'wiktor': 44,
    'oliwia': 7,
    'julia': 21,
}


# ZADANIE 6.3
# GLOSARIUSZ
# Wypisz 5 slow z programowania jako klucz i zapisz ich znaczenie
# Kazde slowo i jego znaczenie wyswietl w postaci elegancko sformatowanych danych wyjsciowych

wordsDefinitions = {
    'inkrementacja': 'Podczas dzialania w petli dodanie 1 lub innej wartosci do zmiennej',
    'jezyk wysokopoziomowy': 'Jezyk programowania skonstruowany tak by byl czytelny dla programisty'
}

increment = wordsDefinitions['inkrementacja']
highLevelLanguage = wordsDefinitions['jezyk wysokopoziomowy']
print(f"Inkrementacja to: \n{increment}")
print(f"Jezyk wysokopoziomowy to: \n{highLevelLanguage}")