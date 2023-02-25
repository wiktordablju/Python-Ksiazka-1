#names.append dodaje do listy na koniec. names.inster(indeks). del names[0] names.popped usuwa ale pozwala na nich wykonywac operacje names.remove(tresc)

#Zadanie 3.4
#Lista gosci
#Jezeli moglbys zaprosic kogokolwiek na obiad, zyjacego lub niezyjacego, to kogo bys zaprosil? Utworz liste zawierajaca przynajmniej trzy osoby. Nastepnie wykorzystaj te liste do wyswietlenia dla kazdej z tych osob komunikaty zapraszajacego ja na obiad
# guests = ['Kurt Cobain', 'Pablo Escobar', 'Elon Musk']
# message = "Zapraszam na obiad"
# print(guests[0], message)
# print(guests[1], message)
# print(guests[2], message)


#Zadanie 3.5
#Zmiana listy gosci
#Dowiedziales sie ze jedna z tych osob nie moze przyjsc na obiad. Konieczne jest wiec wyslanie nastepnych zaproszen. Zastanow sie kogo jeszcze zaprosisz.
#wyswietl kto nie moze przyjsc, zmodyfikuj liste i dane goscia ktory nie bedzie mogl przyjsc na obiad, zastap danymi nowej zaproszonej osoby. Wyswietl drugi zestaw komunikatow z zaproszeniem po jednym komunikacie dla kazdej osoby znajdujacej sie na liscie
# guests = ['Kurt Cobain', 'Pablo Escobar', 'Elon Musk']
# message = "Zapraszam na obiad"

# print(guests[0], message)
# print(guests[1], message)
# print(guests[2], message)

# print(F"{guests[1]} nie może przyjść bo nie żyje")
# guests[0] = 'Ronalidnho Gaucho'
# print(guests[0], message)
# print(guests[1], message)
# print(guests[2], message)

#Zadanie 3.6
#Wiecej gosci
#Znalazles wiekszy stol co oznacza wiecej miejsca dla gosci. Zastanow sie wiec nad jeszcze trzema osobami ktore moglbys zaprosic na obiad
#wyswietl ze znalazles wiekszy stol, insertem dodaj nowego goscia na poczatku, insertem w srodku i appendem na koncu lsity. Wyswietl nmowy zestaw komunikatow z zaproszeniem
# guests = ['Kurt Cobain', 'Pablo Escobar', 'Elon Musk']
# message = "Zapraszam na obiad"
# print("Znaleziono większy stół") 
# guests.insert(0, "Dawid Czerwiak")
# guests.insert(2, "H.P. Lovecraft")
# guests.append('Michał Baron')
# print(guests[0], message)
# print(guests[1], message)
# print(guests[2], message)
# print(guests[3], message)
# print(guests[4], message)
# print(guests[5], message)


#Zadanie 3.7
#Kurczaca sie lsita gosci
#Okazalo sie ze wiekszy stol nie zostanie dostarczony na czas i dlatego masz miejsce jedynie dla dwoch gosci
#printuj ze mozesz miec tylko dwoch gosci, popem usuwaj po jednym gosciu z listy az zostana tylko dwie osoby, po usunieciu kazdej wyswietl komunikat z przeprosinami
# guests = ['Kurt Cobain', 'Pablo Escobar', 'Elon Musk']
# message = "Zapraszam na obiad"
# guests.insert(0, "Dawid Czerwiak")
# guests.insert(2, "H.P. Lovecraft")
# guests.append('Michał Baron')

# print("Niestety stół nie zostanie dostarczony na czas")
# deleted_guest = guests.pop(0)
# print(deleted_guest, "przepraszam za odwołanie obiadu")
# deleted_guest = guests.pop(0)
# print(deleted_guest, "przepraszam za odwołanie obiadu")
# deleted_guest = guests.pop(0)
# print(deleted_guest, "przepraszam za odwołanie obiadu")
# deleted_guest = guests.pop(0)
# print(deleted_guest, "przepraszam za odwołanie obiadu")

# print(guests[0], "zapraszam na obiad")
# print(guests[1], "zapraszam na obiad")
# del guests[0]
# del guests[0]

# print(guests)