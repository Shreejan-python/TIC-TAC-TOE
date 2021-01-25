print("Chose the alphabet(Remember you have only 10 lives to complete the quest)")
Guesses = 1
while(Guesses<=5):
    num = input("I am an alphabet, which is starting of an amphibian,\n I lie before the alphabet of before the alphabet of the starting of the word humanion. Guese the aplphabet:")
    if num<'f':
        print("Enter a greater alphabet than this")
    elif num>'f':
        print("Enter a smaller alphabet than this")
    else:
        print("You chose the correct alphabet. Press C to continue")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1

a = input("Here You need to give your choice:")
while(a=='C'):
    num1 = input("You play with this toy and fly high in the sky with the help of a thread\n chose the alphabet nor you will lose the quest :")
    if num1<'k':
        print("Enter a greater alphabet")
    elif num1>'k':
        print("Enter a greater alphabet")
    else:
        print("You chose the correct alphabet. Press D to continue")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1

b = input("Here you need to give your choice :")
while(b=='D'):
    num2 = input("I am an alphabet starting of a word which is a place  for keeping animals and also an area of crossing the road :")
    if num2<'z':
        print("Enter a greater alphabet than this")
    elif num2>'z':
        print("Enter a smaller alphabet than this")
    else:
        print("You chose the correct alphabet. Press Z to continue")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1

c = input("Here you need to give your choice :")
while(c=='Z'):
    num3 = input("I am an alphabet which is a vowel\n if you eat this you will stay away from doctors :")
    if num3<'a':
        print("Enter a greater alphabet than this")
    elif num3>'a':
        print("Enter a smaller number than this")
    else:
        print("You chose the correct alphabet. Press A to continue")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1

d = input("Here you need to give your choice :")
while(d=='A'):
    num4 = input("I am an alphabet which is a vowel and I come first,\n when you feel cold when you touch solid state of water")
    if num4<'i':
        print("Enter a greater alphabet than this")
    elif num4>'i':
        print("Enter a smaller alphabet than this")
    else:
        print("You chose the correct alphabet. Enter C to continue")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1

e = input("Enter your choice here :")
while(e=='C'):
    num5 = input("I am an alphabet which not a vowel but a consonant\n I take the shape of mine when you half-open your zip")
    if num5<'y':
        print("Enter a greater alphabet than this")
    elif num5>'y':
        print("Enter a smaller alphabet than this")
    else:
        print("Congratualations!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n You wooonnn the quest of alphabet")
        break
    print(10 - Guesses, "number of guesses left")
    Guesses = Guesses + 1
    




    if Guesses>10:
        print("Game Over")  