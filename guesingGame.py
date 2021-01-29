yourNum = input("Enter a number between 1-10: ")
print("yourNum")
i=0

while(i<6)
    if(int(yourNum) < 7):
        print("Number is too low please try again")
    elif(int(yourNum) > 7):
        print("Number is too high please try again")
    else
        print("You guessed the correct number!")