from random import randint, choice

# ZADANIE 9.13
# KOSCI DO GRY
# Przygotuj klase Die z jednym atrybutem o nazwie sides, którego wartoscia domysina bedzie 6. 
# Utworz metode o nazwie roll_die(), wyswietlajaca losowo wygenerowana liczbe z zakresu od 1 do wartosci okreslonej prez liczbe scianek na kosci do gry. 
# Utworz kosc zawierajaca szesc scianek i zasymuluj rzucenie nia 10 razy.
# Pozniej utworz kosci zawierajace 10 i 20 scianek.
# Kazda nowa koscia rzut 10 razy.


class Die():
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

my_cube = Die(6)

i=0
while True:
    my_cube.roll_die()
    i += 1
    if i == 6:
        break
    
print("\n-------------------------------------------------------")
    
cube_10 = Die(10)
cube_20 = Die(20)

i=0
while True:
    cube_10.roll_die()
    i += 1
    if i == 10:
        break
    
print("\n-------------------------------------------------------")

i=0
while True:
    cube_20.roll_die()
    i += 1
    if i == 10:
        break


# ZADANIE 9.14
# LOTERIA
# Utworz liste lub krotke zawierajaca serie dziesieciu liczb i pieciu liter. 
# Losowo wybierz cztery liczby lub litery z listy, a nastepnie wyswietl komunikat informujacy, ze kupon zawierajacy liczby lub litery dopasowane do wylosowanych wygrywa nagrode.


numbers_letters = [1, 2, 3, 4, 5, 'q', 'w', 'e', 'r', 't', 6, 7, 8, 9, 10]
winning_numbers_letters = []

while True:
    winning_numbers_letters.append(choice(numbers_letters))
    if len(winning_numbers_letters) == 4:
        break

print("Wygrywajace liczby:")
for number_letter in winning_numbers_letters:
    print(number_letter)
        

# ZADANIE 9.15
# ANALIZA LOTERI
#  Wykorzystaj petle do ustalenia, jak trudno jest wygrac w loterii, ktra modelowales w poprzednim cwiczeniu. 
# Utworz liste lub krotke o nazwie my_ticket. 
# Nastepnie zdefiniuj petle losujaca liczby dopôty, dopóki nie zostana dopasowane do Twojego kuponu. 
# Wyswietl komunikat informujacy, ile iteracji petli trzeba bylo wykonac, zanim padly liczby znajdujace sie na Twoim kuponie.


numbers_letters = [1, 2, 3, 4, 5, 'q', 'w', 'e', 'r', 't', 6, 7, 8, 9, 10]
winning_numbers_letters = []

while True:
    winning_numbers_letters.append(choice(numbers_letters))
    if len(winning_numbers_letters) == 4:
        break

my_ticket = [7, 'e', 'r', 3]

number_of_tries = 0
while my_ticket != winning_numbers_letters:
    number_of_tries += 1
    print(f"Próba: {number_of_tries}")
    winning_numbers_letters = []
    while True:
        winning_numbers_letters.append(choice(numbers_letters))
        if len(winning_numbers_letters) == 4:
            break
else:
    print(f"Wygrałeś za {number_of_tries} razem")