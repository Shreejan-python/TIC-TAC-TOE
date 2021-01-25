import random
toss = input("Head(H) or tails(T)")
toss_list = ['H', 'T']
#comprandtoss = random.choice(toss_list)

print("Computer has chosen")
print(f"You chose {toss}")

randtoss = random.choice(toss_list)
print(f"The result is {randtoss}")


if randtoss==toss:
    print("You won the toss !")
    cn = input("Bat(B) or Ball(L)")
    run = 0
    randrun = 0
    while cn=='B':
        #run_list = [1, 2, 3, 4, 5, 6]
        run_1 = int(input("Put a number between 1 to 6 : "))
        randomball = random.randint(1, 6)
        print(f"Computer gave {randomball}")
        run = run_1 + run
        print("Your total run is : ", run)
        if randomball==run_1:
            print('out')
            choice = input("Do you want to continue ? Y for yes and N for no")
            if choice=='Y':
                run_of_comp = 0
                while(run_of_comp<run):
                    ball = int(input("You are balling. Enter a number between 1 to 6 : "))
                    randomrun = random.randint(1, 6)
                    print(f"Computer gave {randomrun}")
                    run_of_comp = run_of_comp + randomrun
                    print(f"Computer's total run is : {run_of_comp}")
                    if run_of_comp>run:
                        print("You lose")
                        exit()
                    elif randomrun==ball:
                        print("You won")
                        exit()
            elif choice=='N':
                print("Computer own the match")
                break


    while cn=='L':
        randr = random.randint(1, 6)
        ball_1 = int(input("You are bowling. Enter a number between 1 to 6: "))
        print(f"Computer gave {randr}")
        randrun = randrun + randr
        print(f"Computer's current run is {randrun}")
        if ball_1==randr:
            print("Out")
            run_of = 0
            while(randrun>run_of):
                run_of_you = int(input("You are batting : "))
                randomball_2 = random.randint(1, 6)
                print(f"Computer gave {randomball_2}")
                run_of = run_of + run_of_you
                print("Your current is ", run_of)
                if randomball_2==run_of_you:
                    print("OUT, you loose")
                    exit()
                elif run_of>randrun:
                    print("You won!!")
                    exit()





elif randtoss!=toss:
    print("comp own")
    bat_ball = ['B', 'L']
    randCN = random.choice(bat_ball)
    if randCN=='B':
        print("Computer chose to bat")
        _run_ = 0
        while randCN=='B':
            randomrun1 = random.randint(1, 6)
            you_ball = int(input("Enter a number between 1 to 6 :"))
            print(f"Computer gave now {randomrun1}")
            _run_ = _run_ + randomrun1
            print("Computer's total run is ", _run_)
            if you_ball==randomrun1:
                print("Out")
                uo_run = 0
                while (uo_run<_run_):
                    randomball_1 = random.randint(1, 6)
                    r = int(input("You are batting. Enter a number between 1 to 6 :"))
                    print(f"Computer gave{randomball_1}")
                    uo_run = uo_run + r
                    print("Your's total run is ", uo_run)
                    if randomball_1==r:
                        print('out')
                        exit()
                    elif uo_run>_run_:
                        print("You won")
                        exit()
    elif randCN=='L':
        print("Computer chose to ball")
        ru_ = 0
        while randCN=='L':
            ur_ = int(input("You are batting enter a number between 1 to 6 :"))
            ra = random.randint(1, 6)
            print(f"Computer gave {ra}")
            ru_ = ru_ + ur_
            print("Your total run is : ", ru_)
            if ra==ur_:
                print("Out")
                r_choice = input("Do you want to continue. Yes(Y) or No (N)")
                if r_choice=='Y':
                    comp_your_rn = 0
                    while(comp_your_rn<ru_):
                        d_ball_ = int(input("Enter a number between 1 to 6"))
                        ughu = random.randint(1, 6)
                        print(f"Computer gave {ughu}")
                        comp_your_rn = comp_your_rn + ughu
                        print("COmputer's total run is ", comp_your_rn)
                        if ughu==d_ball_:
                            print("Out, you won")
                            exit()
                        elif comp_your_rn>ru_:
                            print("You loose")
                elif r_choice=='N':
                    print("Computer own")

