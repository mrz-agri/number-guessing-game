import random

class Guess:
    def __init__(self):
        self.number = random.randint(1, 100)

    def guess_number(self):
        counter = 1
        while counter <= 8:
            guessed = int(input("Guess: "))

            if guessed == self.number:
                print("Well Done! That's it!")
                break
            elif guessed > self.number + 5:
                print("Too high")
            elif self.number < guessed < self.number + 5:
                print("Almost There! A bit high")
            elif guessed < self.number - 5:
                print("Too low!")
            elif self.number - 5 <= guessed < self.number:
                print("Almost There! A bit low")

            counter += 1
        else:
            print(f"Game over! The answer was {self.number}")

        again = input("Would you like to play again? (type ok to start, any key to exit): ").lower()
        if again == "ok":
            self.number = random.randint(1, 100)
            self.guess_number()
        else:
            print("Bye!")

start = input("I make a number between 1 to 100. You can guess it for 8 times. Ok? (type ok to start and any key to escape): ").lower()
if start == "ok":
    Guess().guess_number() 
