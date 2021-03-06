from random import randint

range1 = randint(1, 100)
number = randint(0, range1)
tries = 0

for i in range(100):
    print("Tries:", tries)
    tries += 1
    guess = int(input("Guess my number: "))
    if number == guess:
        print("You did it!")
        print("Tries:" , tries)
        break
    else:
        print("Nope!")
        hint = input("Do you want hint?(yes/no) ")
        if hint == "yes":
            what_hint = input("Choose your hint(type it!): range, greater/smaller, multiple, divisible: ")
            #range hint
            if what_hint == "range" or what_hint == "r":
                print("My number is between", "0" + " and", range1 + 1)
            #greater/smaller
            elif what_hint == "greater/smaller" or what_hint == "g/s":
                if number < guess:
                    print("Your guess is greater than my number!")
                else:
                    print("Your guess is smaller than my number!")
            elif what_hint == "multiple" or what_hint == "m":
                if number%2 == 0:
                    print("My number is multiple of 2!")
                if number%3 == 0:
                    print("My number is multiple of 3!")
                if number%5 == 0:
                    print("My number is multiple of 5!")
                if number%10 == 0:
                    print("My number is multiple of 10!")
            elif what_hint == "divisible" or what_hint == "d":
                if number%2 == 0:
                    print("My number is divisible with 2!")
                if number%3 == 0:
                    print("My number is divisible with 3!")
                if number%5 == 0:
                    print("My number is divisible with 5!")
                if number%10 == 0:
                    print("My number is divisible with 10!")
            else:
                print("Enter a valid hint next time!")
        elif hint == "no":
            continue
        else:
            print("I will take that as no!")
            
        continue
    

