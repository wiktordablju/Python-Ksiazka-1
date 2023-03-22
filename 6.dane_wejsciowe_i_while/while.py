
# ZADANIE 7.4
#  DODATKI DO PIZZY 
# Utwórz petle proszaca uzytkownika o podanie seri dodatkow do pizzy. Dzialanie petli powinno zostad zakonczone, kiedy zostanie wpisane slowo 'koniec'. Gdy uzytkownik bedzie podawac kolejne dodatki. petla powinna wyswietiac komunikat o dodaniu danego sktadnika do pizzy.

print("Wybierz dodatki do pizzy, na slowo 'koniec' zakonczy sie pobieranie")
ingridients = []

while True:
    ingridient = input("\nWybierz dodatek do pizzy: ")
    
    if ingridient == 'koniec':
        break
    else:
        print(f"Dodalismy {ingridient} do twojej pizzy")
        

# ZADANIE 7.5
# BILETY DO KINA
# Cena biletu do kina jest uzalezniona od wieku widza. Jezeli widz ma ponizej 3 lat, bilet jest bezplatny. Dia dzieci w wieku od 3 do 12 lat bilet kosztuje 10 zl. 
# Dla osob wieku powyzej 12 lat cena biletu wynosi 15 zl.
# Utworz petle proszaca uzytkownika o podanie wieku, a nastepnie na podsta-wie otrzymanych danych wyswietl komunikat zawierajacy prawidtowa cene biletu.

message = "Podaj swoj wiek: "

while True:
    age = input("\n Podaj swoj wiek: ")
    age = int(age)
    
    if age <= 3:
        print("\nBilet jest bezplatny")
        break
    elif age <=12:
        print("\nBilet kosztuje 10 zl")
        break
    elif age > 12:
        print("\nBilet kosztuje 15zl")
        break


