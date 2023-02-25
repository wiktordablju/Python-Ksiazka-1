# Zadanie 4.3
# Odliczanie do dwudziestu
# Uzyj petli for do wyswietlenia liczb od 1 do 20 wlacznie
# for number in range (1,21):
#     print(number)


# Zadanie 4.4
# Milion
# Utworz liste liczb od jednego do miliona a nastepnie wyswietl ja za pomoca petli for
# numbers=[]
# for number in range(1,1_000_001):
#     numbers.append(number)
# print(numbers)


# Zadanie 4.5
# Sumowanie do miliona
# Utworz liste liczb od jednego do miliona a nastepnie za pomoca funkcji min i max sprawdz czy lista ffaktycznie zaczyna sie od wartosci jeden i konczy na milione, uzyj funkcje sum aby zobaczyc jak szybko python moze dodac milion liczb
# numbers=[]
# for number in range(1,1_000_001):
#     numbers.append(number)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


# Zadanie 4.6
# Liczby nieparzyste
# Za pomoca trzeceiego argumentu funkcji range utworz liste liczb nieparzystych z zakresu od 1 do 20 a nastepnie wyswietl je za pomoca petli for
# numbers=[]
# for number in range(1,21,2):
#     numbers.append(number)
# for number in numbers:
#     print(number)
    

# Zadanie 4.7
# Trzy
# Utworz liste liczb od 3 do 30 podniesionych do potegi trzeciej a nastepnie wyswietl zawartosc listy za pomoca petli for
# numbers=[]
# for number in range(3,31):
#     numbers.append(number**3)
# for number in numbers:
#     print(number)


# Zadanie 4.8
# Szcescian
# Liczba podniesiona do trzeciej potegi jest nazywana szescianem, na przyklad szczescia liczby 2 to 2**3. Utworz liste pierwszych dziesieciu szczescianow an astepnie je wyswietl forem
# numbers=[]
# for number in range(1,11):
#     numbers.append(number**3)
# for number in numbers:
#     print(number)


# Zadanie 4.9
# Szescian za pomoca listy skladanej
# Wykorzystaj liste skladana do wygenerowania listy pierwszych dziesieciu szescianow 
# numbers=[number**3 for number in range(1,11)]
# for number in numbers:
#     print(number)