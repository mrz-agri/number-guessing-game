class Guess:
    def __init__(self, number, guessed):
        self.number = number
        self.guessed = guessed

    def guess_number (self):
        counter = 1
        while  counter < 8:

            if self.guessed == self.number:
                print("Well Done! That's it!")
                break

            elif self.guessed > (self.number + 1):
                print("Too high")
                
            elif self.guessed > self.number and self.guessed < (self.number + 5):
                print("Almost There! A bit high")
                
            elif self.guessed < (self.number - 5):
                print("Too low!")
                

            elif self.guessed < self.number and self.guessed >= (self.number - 5):
                print("Almost There! A bit low")

            counter += 1    
            if counter < 8:
                print(f"Try again ({9-counter} guesses left): ")
                self.guessed = int(input())

            else:
                print("Game over! you 'v used all 8 tries")
                print(f"The answer is {self.number}")



answer = input ("I make a number between 1 to 100. You can guess it for 8 times. Ok? (type ok for start and any key for escape): ")
if answer == "Ok" or answer == "ok":
    import random
    number = random.randint(1, 100)
    guessed = int(input("Guess the number: "))
    game = Guess(number, guessed)
    game.guess_number()
else:
    quit()