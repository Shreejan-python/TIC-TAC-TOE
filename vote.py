print("Welcome to vote counter")

voters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nominee_1=input("Nominee 1 name :")
nominee_2=input("Nominee 2 name :")

print("This year's nominees are :", nominee_1, ",", nominee_2)

nom_1_votes = 0
nom_2_votes = 0

voters_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_of_voters = len(voters_id)

while True:
    if voters_id==[]:
        print("Voting session is over")
        if nom_1_votes>nom_2_votes:
            print("This year's winner is :", nominee_1, "with, ", percent)
            break
        elif nom_2_votes>nom_1_votes:
            print("This year's winner is :", nominee_2)
            print("This year's winner is :", nominee_2, "with, ", percent1)
            break
    else:
        voter = int(input("Enter your voter id :"))
        if voter in voters_id:
            print("You are voter ")
            voters_id.remove(voter)
            vote = int(input("Enter 1 for nominee-1 & 2 for nominee-2"))
            if vote==1:
                nom_1_votes+=1
                print("Thank you for casting vote")
            elif vote==2:
                nom_2_votes+=1
                print("Thankyou for casting vote")
        else:
            print("You are not voter of this area")
