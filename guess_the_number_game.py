number = 19
your_guess = int(input("enter your guess :"))
while your_guess != number :
    if your_guess < number:
        print("too low , larger your number .")
    elif your_guess > number :
        print("too high , smaller your number .")
    your_guess = int(input("your guess : "))
print("yeah , you got it right !!!")