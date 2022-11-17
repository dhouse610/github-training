##Functions##
# Spanish: gracias
# Mandarin: xie xie ni
# Portuguese: obrigada
# French: merci
# German: danke
# Croatian: hvala vam
# English: thank you

def Thanks(name, language = "english"):
    try:
        if language.upper() == "ENGLISH":
            word = "Thank you"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "SPANISH":
            word = "Gracias"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "MANDARIN":
            word = "Xie xie ni"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "PORTUGUESE":
            word = "Obrigada"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "FRENCH":
            word = "Merci"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "GERMAN":
            word = "Danke"
            givethanks = f"{word}, {name}"
            correct = 0
        elif language.upper() == "CROATIAN":
            word = "Hvala vam"
            givethanks = f"{word}, {name}"
            correct = 0
        else:
            print("Incorrect Input, try again")
            return
        return givethanks
    except:
        print("Incorrect Input, try again")
        return

thank1 = Thanks("Davis", "German")
thank2 = Thanks("Davis")
#thank2 = Thanks()
#print(thank1)


##Book Sorting##

#Book Categories
#Volume I - A to B
#Volume II - C to Ch
#Volume III - Ci to Cz
#Volume IV - D to G
#Volume V - H to K
#Volume VI - L to N
#Volume VII - O to P
#Volume VIII - Q to S
#Volume IX - T to W
#Volume X - X to Z
#Volume XI - Numbers

def BookSort(inBook):
    try:
        inBook = str.split(inBook, " ")
        if inBook[0].upper() == 'A' or inBook[0].upper() == 'AN' or inBook[0].upper() == 'THE':
            startPos = 1
        else:
            startPos = 0
        if 'A' <= inBook[startPos][0].upper() <= 'B':
            sorted = f'{" ".join(inBook)} is in Volume I'
        elif 'C' == inBook[startPos][0].upper()[startPos]:
            if 'A' <= inBook[startPos][1].upper() <= 'H':
                sorted = f'{" ".join(inBook)} is in Volume II'
            elif 'I' <= inBook[startPos][1].upper() <= 'Z':
                sorted = f'{" ".join(inBook)} is in Volume III'
        elif 'D' <= inBook[startPos][0].upper() <= 'G':
            sorted = f'{" ".join(inBook)} is in Volume IV'
        elif 'H' <= inBook[startPos][0].upper() <= 'K':
            sorted = f'{" ".join(inBook)} is in Volume V'
        elif 'L' <= inBook[startPos][0].upper() <= 'N':
            sorted = f'{" ".join(inBook)} is in Volume VI'
        elif 'O' <= inBook[startPos][0].upper() <= 'P':
            sorted = f'{" ".join(inBook)} is in Volume VII'
        elif 'Q' <= inBook[startPos][0].upper() <= 'S':
            sorted = f'{" ".join(inBook)} is in Volume VIII'
        elif 'T' <= inBook[startPos][0].upper() <= 'W':
            sorted = f'{" ".join(inBook)} is in Volume IX'
        elif 'X' <= inBook[startPos][0].upper() <= 'Z':
            sorted = f'{" ".join(inBook)} is in Volume X'
        elif '0' <= inBook[startPos][0].upper() <= '9':
            sorted = f'{" ".join(inBook)} is in Volume XI'
        return sorted
    except:
        print("Invalid book input, try again")
        return


def GetWord(inBook):
    inBook = str.split(inBook, " ")
    if inBook[0].upper() == 'A' or inBook[0].upper() == 'AN' or inBook[0].upper() == 'THE':
        return inBook[1]
    else:
        return inBook[0]

def SortWord(word):
    if 'A' <= word.upper()[0] <= 'B':
        return 'I'
    elif 'C' == word.upper()[0]:
        if 'A' <= word.upper()[1] <= 'H':
            return 'II'
        elif 'I' <= word.upper()[1] <= 'Z':
                return 'III'
    elif 'D' <= word.upper()[0] <= 'G':
        return 'IV'
    elif 'H' <= word.upper()[0] <= 'K':
        return 'V'
    elif 'L' <= word.upper()[0] <= 'N':
        return 'VI'
    elif 'O' <= word.upper()[0] <= 'P':
        return 'VII'
    elif 'Q' <= word.upper()[0] <= 'S':
        return 'VIII'
    elif 'T' <= word.upper()[0] <= 'W':
        return 'IX'
    elif 'X' <= word.upper()[0] <= 'Z':
        return 'X'
    elif '0' <= word.upper()[0] <= '9':
        return 'XI'


def SortBook(bookTitle):
    try:
        word = GetWord(bookTitle)
        volume = SortWord(word)
        return f'{bookTitle} is in Volume {volume}'
    except:
        print("INVALID INPUT")
        return





