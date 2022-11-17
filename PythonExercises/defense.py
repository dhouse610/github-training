##Defensive Grade Calculator###
totalPoints = 100
studentName = "Davis"
try:
    score = float(input("Enter Score: "))
    score = round(score,2)
    percentage = score/totalPoints*100
    if 100 >= percentage >= 90:
        grade = 'A'
    elif 90 > percentage >= 80:
        grade = 'B'
    elif 80 > percentage >= 70:
        grade = 'C'
    elif 70 > percentage >= 60:
        grade = 'D'
    elif 60 > percentage >= 0:
        grade = 'F'
    print(f"{studentName}'s letter grade is {grade} because they got a {score} out of {totalPoints}")
except:
    print("Invalid Input")


###Defensive Book Classification###
books = "ULYSSES, THE GREAT GATSBY, A PORTRAIT OF THE ARTIST AS A YOUNG MAN, LOLITA, BRAVE NEW WORLD, THE SOUND AND THE FURY, CATCH-22, DARKNESS AT NOON, SONS AND LOVERS, THE GRAPES OF WRATH, UNDER THE VOLCANO"
bookList = str.split(books, ", ")

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
try:
    inBook = input("Enter Book Title: ")
    inBook = str.split(inBook, " ")
    if inBook[0].upper() == 'A' or inBook[0].upper() == 'AN' or inBook[0].upper() == 'THE':
        startPos = 1
    else:
        startPos = 0
    if 'A' <= inBook[startPos][0].upper() <= 'B':
        print(f'{" ".join(inBook)} is in Volume I')
    elif 'C' == inBook[startPos][0].upper()[startPos]:
        if 'A' <= inBook[startPos][1].upper() <= 'H':
            print(f'{" ".join(inBook)} is in Volume II')
        elif 'I' <= inBook[startPos][1].upper() <= 'Z':
            print(f'{" ".join(inBook)} is in Volume III')
    elif 'D' <= inBook[startPos][0].upper() <= 'G':
        print(f'{" ".join(inBook)} is in Volume IV')
    elif 'H' <= inBook[startPos][0].upper() <= 'K':
        print(f'{" ".join(inBook)} is in Volume V')
    elif 'L' <= inBook[startPos][0].upper() <= 'N':
        print(f'{" ".join(inBook)} is in Volume VI')
    elif 'O' <= inBook[startPos][0].upper() <= 'P':
        print(f'{" ".join(inBook)} is in Volume VII')
    elif 'Q' <= inBook[startPos][0].upper() <= 'S':
        print(f'{" ".join(inBook)} is in Volume VIII')
    elif 'T' <= inBook[startPos][0].upper() <= 'W':
        print(f'{" ".join(inBook)} is in Volume IX')
    elif 'X' <= inBook[startPos][0].upper() <= 'Z':
        print(f'{" ".join(inBook)} is in Volume X')
    elif '0' <= inBook[startPos][0].upper() <= '9':
        print(f'{" ".join(inBook)} is in Volume XI')
except:
    print("Invalid book input, try again:(")
