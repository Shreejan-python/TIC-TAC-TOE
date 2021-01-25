import random
def game(a, b):

    if a == b:
        return None
    elif a == 's':
        if b == 'sc':
            return False
        elif b == 'p':
            return True
    elif a == 'p':
        if b == 's':
            return False
        elif b == 'sc':
            return True
    elif a == 'sc':
        if b == 'p':
            return False
        elif b == 's':
            return True






print("Computer Turn: Stone(s) paper(p) scissors(sc)")
randNo = random.randint(1, 3)
# print(randNo)
if randNo == 1:
    a = 's'
elif randNo == 2:
    a = 'p'
elif randNo == 3:
    a = 'sc'





b = input("Your's Turn: Stone(s) paper(p) scissors(sc)")

print(f"Computer chose\n {a}")
print(f"You chose\n {b}")
c = game(a, b)
if c == None:
    print("Game is tie")
elif c:
    print("You win")
else:
    print("You loose")