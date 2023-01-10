
while True:

    answer = input("Would you like to play? (yes/no) ")

    if answer.lower().strip() == "yes":

        answer = input("You just robbed a bank, would you like to take the roof to exit or back door? (roof/back)").lower().strip()
        if answer == "roof":
            answer = input("You encounter a fbi agent, would you like to run or shoot. (run/shoot)")

            if answer == "shoot":
                print("Too bad your shot first!, you lost!")
            else:
                print("Good choice, you made it away safely.")

                answer = input("You see an open window on the other building, or a fire escape route. Which would you like to take? (window/fire)")

                if answer == "fire":
                    print("The ladder was loose and you fall, You Lost!")

                else:
                    print("You got away, Congrats!")




        elif answer == "back":
            print("You run into an a cop and get arrested. Game Over!")


        else:
            print("Invalid choice, you lost!")



    else:
        print("That's too bad!")
        break