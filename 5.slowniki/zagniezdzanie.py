# ZADANIE 6.7
# OSOBY
# Zacznij od programu z zadania 6.1
# Utworz dwa nowe slowniki przedstawiajace rozne osoby a nastepnie umeisc je w liscie people
# Przeprowadz iteracje przez liste osob i wyswietl wszystkie informacje o poszczegolnych osobach

wiktorDziendziel = {
    'name':  'wiktor',
    'surname': 'dziendziel',
    'age': 18,
    'city': 'siemianowice slaskie',
}

kamilMrowiec = {
    'name':  'kamil',
    'surname': 'mrowiec',
    'age': 18,
    'city': 'siemianowice slaskie',
}

oliwierKotlicki = {
    'name':  'oliwier',
    'surname': 'kotlicki',
    'age': 17,
    'city': 'czeladz',
}

people = [wiktorDziendziel, kamilMrowiec, oliwierKotlicki]
for guy in people:
    print(guy)


# ZADANIE 6.8
# ZWIERZETA
# Utworz kilka slownikow i nadaj im nazwy zwierzat
# W kazdym slowniku umiesc informacje o wlascicielach tych zwierzat
# Slowniki powinny byc na liscie pets
# Przeprowadz iteracje i wyswietl informacje o poszczegolnych zwierzetach

dog = {
    'name': 'Kropka',
    'owner': "Wiktor"
}

cat = {
    'name': 'Teo',
    'owner': "Emilia"
}

parrot = {
    'name': 'Albercik',
    'owner': 'Kamil'
}

pets = [dog, cat, parrot]
for pet in pets:
    print(pet)


# ZADANIE 6.9
# ULUBIONE MIEJSCA
# Utworz slownik o nazwie favoriteplaces i pomysl o trzech imionych i uzyj ich jako klucz slownika
# Kazdej osobie przypisz po 3 ulubione miejsca
# Wyswietl ulubione miejsca kazdej osoby

favoritePlaces = {
    'Wiktor': ['seul', 'warszawa', 'londyn'],
    'Oliwia': ['londyn', 'rzym', 'barcelona'],
    'Kamil': ['rabka', 'katowice', 'sevilla']
    
}

for name, places in favoritePlaces.items():
    print(f"\nUlubionymi miejscami {name.title()} są:")
    for place in places:
        print(place.title())
        


# ZADANIE 6.10
# ULUBIONE LICZBY
# Zmodyfikuj program z 6.2 
# Kazda osoba ma miec wiecej niz 1 ulubiona liczbe
# Wyswietl kazda ulubiona liczbe osob

favoriteNumbers = {
    'kamil': [14, 7, 21],
    'wiktor': [44, 21, 7],
    'oliwia': [7, 11, 24],
    'julia': [21, 22, 23],
}

for name, numbers in favoriteNumbers.items():
    print(f"\nUlubionymi liczbami {name.title()} są:")
    for number in numbers:
        print(number)


# ZADANIE 6.11
# MIASTA
# Utworz slownik cities i jako klucze podaj trzy miasta
# do kazdego utworz oddzielny slownik zawierajace informacje o tym miescie
# Wyswietl informacje o kazdym z miast


cities = {
    'Seul': {
        'country': 'korea poludniowa',
        'population': 9_700_000,
        'fact': 'Seul to stolica Koreii Południowej'  
    },
    'Szanghaj': {
        'country': 'chiny',
        'population': 26_032_000,
        'fact': 'Szanghaj to najwieksze miasto Chin'  
    },
    'Katowice': {
        'country': 'polska',
        'population': 302_397,
        'fact': 'Katowice to najwieksze miasto slaska'  
    },
}

for city, cityInformations in cities.items():
    print(f"Nazwa miasto to: {city.title()}")
    print(f" ,należy do kraju {cityInformations['country']}, ma populację {cityInformations['population']} a faktem o nim jest to że: {cityInformations['fact']} ")
