 # ZADANIE 6.4
# GLOSARIUSZ 2
# Zmodyfikuj kod z cwiczenia 6.3
# Zastap print petla

wordsDefinitions = {
    'inkrementacja': 'Podczas dzialania w petli dodanie 1 lub innej wartosci do zmiennej',
    'jezyk wysokopoziomowy': 'Jezyk programowania skonstruowany tak by byl czytelny dla programisty'
}

for word, definition in wordsDefinitions.items():
    print(f"{word} oznacza: {definition}")


# ZADANIE 6.5
# RZEKI
# Utworz slownik zawierajacy 3 rzeki oraz kraje przez tkore plyna
# Wykorzystaj petle ktora pokazuje kazda wartosc
# Wykorzystaj petle do pokazania wszystkich rzek oraz panstw

rivers = {
    'nil': 'egipt',
    'wisla': 'polska',
    'tamiza': 'anglia',
}

print("Kraje uzyte w slowniku")
for country in rivers.values():
    print(country.title())
    
print("\nRzeki uzyte w slowniku")
for river in rivers.keys():
    print(river.title())


# ZADANIE 6.6
# ANKIETA
# Uzyj favorite languages
# Utworz liste osob ktore powinny wziac udzial w ankiecie
# Umiesc pewne osoby ktore juz znalazly sie w slowniku
# Przeprowadz iteracje po ankiecie, jesli dana osoba wziela udzial wyswietl ze dziekujesz a ta co nie ze zapraszasz

languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'pawel': 'python',
}

pretendents = ['janek', 'kryspin', 'julia']

for language in languages.keys():
    if language in pretendents:
        for pretendend in pretendents:
            print(f"{pretendend} powinenes wziac udzial w ankiecie")
    else :
        print(f"{language} dzieki za udzial w ankiecie")