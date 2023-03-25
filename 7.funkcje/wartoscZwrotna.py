# ZADANIE 8.6
# NAZWY MIAST
# Utworz funkcje o nazwie city_country () pobierajaca nazwe miasta i kraju, w którym ono lezy.
# Przygotowana funckje wywotaj z przynajmniej trzema parami miasto-pañstwo i wyswietl wygenerowana prez nie wartosc.

def cityCountry(city, country):
    """Wyswietla pare miasto-panstwo"""
    return(f"{city.title()}-{country.title()}")

pair = cityCountry('katowice', 'polska')
print(pair)
    

# ZADANIE 8.7
# ALBUM
# tworz funkcje o nazwie make_album() odpowiedzialna za zbudowanie slownika reprezentujacego album muzyczny. 
# funckja powinna pobrac nazwe zespolu lub artysty oraz tytul albumu.
# Wartoscia, zwrotna funkcji  powinien byc stownik zawierajacy te dwa fragmenty informacji. 
# Za pomoca przygotowanej funkcji utwörz try stowniki przedstawiajace rózne album. Wyswiet! kazda wartosc zwrotna, aby pokazac, ze stowniki prawdilowo przechowuja informace o albumach.
# Wykorzystujac wartosc specjalna None, do funkcji make_album() dodaj opcjonalny parametr pozwalajacy na przechowywanie liczby utworw znajdujacch sie na plycie. Jezeli wywotanie funkcji bedzie zawierato wartosé dla licaby utworów, nalezy ja dodac do stownika informacji o albumie.
# Zdefinjuj co najmniej jedno now wywolanie funkcji obejmujace takie liczbe utworw na plycie.

def makeAlbum(arist, title, songs=None):
    """Tworzy dictionary przechowujace informacje o albumie muzycznym"""
     
    info = {
        'name': arist,
        'title': title,
    }
    if songs:
        info['songs'] = songs
    
    return info

imprimatur = makeAlbum('deys', 'imprimatur')
print(imprimatur)

futura = makeAlbum('schafter', 'futura', songs=15)
print(futura)


# ZADANIE 8.8
# ALBUMY UZYTKOWNIKOW
# Prace rozpocznij od programu utworzonego w cwiczeniu 8.7. 
# Dodaj petle while pozwalajaca uzytkownikom a wprowadzenie artysty i tytulu plyty. Po zebraniu tych informacji wywotaj funkcie makealbum() wraz z podanymi przez uzytkownika danymi wejsciowymi oraz wyswieti slownik utworzony przez program. Upewnij sie, ze zdefiniowales wartosc pozwalajaca opuscic petle while.

def makeAlbum(arist, title, songs=None):
    """Tworzy dictionary przechowujace informacje o albumie muzycznym"""
     
    info = {
        'artist': arist,
        'title': title,
    }
    if songs:
        info['songs'] = songs
    
    return info

while True:
    print("Podawaj informacje o swoim ulubionym albumie" )
    print("(Jesli chcesz wyjsc, w dowolnym momencie wpisz 'stop') ")
    
    artist = input("Podaj artyste/grupe ktora stworzyla ten album ")
    if artist == 'stop':
        break
    
    title = input("Podaj nazwe albumu ")
    if title == 'stop':
        break
    
    songsQuestion = input("Czy chcesz podac ilosc piosenek? (tak/nie) ")
    if songsQuestion == 'tak':
        songs = input("Podaj ilosc piosenek ")
        if songs == 'stop':
            break
    elif songsQuestion == 'stop':
        break
    else:
        songs = None
            
    title = makeAlbum(artist, title, songs)
    print(title)