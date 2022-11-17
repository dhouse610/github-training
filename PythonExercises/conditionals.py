###Grade Calculator###
totalPoints = 100
score = 49
studentName = "Davis"

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


###Book Classification###
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

for book in bookList:
    if book.upper()[:2] == 'A ' or book.upper()[:3] == 'AN ' or book.upper()[:4] == 'THE ':
        startPos = book.find(' ') + 1
    else:
        startPos = 0
    if 'A' <= book.upper()[startPos] <= 'C':
        print(f'{book} is in Volume I')
    elif 'D' <= book.upper()[startPos] <= 'F':
        print(f'{book} is in Volume II')
    elif 'G' == book.upper()[startPos]:
        if 'A' <= book.upper()[startPos+1] <= 'O':
            print(f'{book} is in Volume III')
        elif 'P' <= book.upper()[startPos+1] <= 'Z':
            print(f'{book} is in Volume IV')
    elif 'H' <= book.upper()[startPos] <= 'K':
        print(f'{book} is in Volume V')
    elif 'L' <= book.upper()[startPos] <= 'M':
        print(f'{book} is in Volume VI')
    elif 'P' <= book.upper()[startPos] <= 'M':
        print(f'{book} is in Volume VII')
    elif 'Q' <= book.upper()[startPos] <= 'S':
        print(f'{book} is in Volume VIII')
    elif 'T' <= book.upper()[startPos] <= 'W':
        print(f'{book} is in Volume IX')
    elif 'X' <= book.upper()[startPos] <= 'Z':
        print(f'{book} is in Volume X')
