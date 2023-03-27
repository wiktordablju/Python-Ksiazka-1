# ZADANIE 8.9
# KOMUNIKATY
# Przygotuj liste zawierajaca serie krötkich komunikatów, a nastepnie przekaz ja do funkcji o nazwie show messages (), która powinna wyswietlic kazdy komunikat umieszczony na tej liscie.

def showCommuniacte(communicates):
    """Wypisuje komunikat po komunikacie z listy komunikatow"""
    for communicate in communicates:
        print(communicate)

communicates = ['hej', 'siemanko', 'czolem', 'czesc']

showCommuniacte(communicates)


# ZADANIE 8.10
# WYSYLANIE KOMUNIKATOW
# Prace rozpocznij od kopii programu z cwiczenia 8.9. 
# Nastepnie utworz funkcje o nazwie send messages (), której zadaniem bedzie wyswietlenie wszystkich komunikatów, a nastepnie przeniesienie ich na nowa liste o nazwie sent messages. 
# Po wywolaniu funkci nalezy wyswietlic obie listy i upewnic sie o prawdilowym przeniesieniu komunikatów.

def sendMessages(communicates, sentMessages):
    """Wyswietla wiadomosc oraz przenosi jej do tablicy z wyslanymi wiadomosciami"""
    while communicates:
        currentMessage = communicates.pop()
        print(currentMessage)
        sentMessages.append(currentMessage)
        
sentMessages = []
communicates = ['hej', 'siemanko', 'czolem', 'czesc']

sendMessages(communicates, sentMessages)


# ZADANIE 8.11
# ZARCHIWIZOWANE KOMUNIKATY
#  Prace rozpocznij od kodu utworzonego w cwiczeniu 8.10. 
# Wywolaj funkcje send messages () wraz z kopia listy komunikatów. 
# Po wywolaniu funkcji wyswieti obie listy, aby pokazac istnienie pierwotnej listy z zachowanymi komunikatami.

def sendMessages(communicates, sentMessages):
    """Wyswietla wiadomosc oraz przenosi jej do tablicy z wyslanymi wiadomosciami"""
    while communicates:
        currentMessage = communicates.pop()
        print(currentMessage)
        sentMessages.append(currentMessage)
        
sentMessages = []
communicates = ['hej', 'siemanko', 'czolem', 'czesc']

sendMessages(communicates[:], sentMessages)

print(sentMessages)
print(communicates)