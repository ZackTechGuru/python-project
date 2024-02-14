my_age = int(input("Enter your age :" ))
if my_age >= 18:
    print(f"{my_age}You are eligible to vote")
    print("Proceed to the next step and cast your vote")
else:
    print(f"{my_age}Your not eligible to vote")
    print("Go home")