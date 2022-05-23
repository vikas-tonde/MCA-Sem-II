import random
def check(number, guess):
    if number == guess:
        return 100
    if number[0] in guess or number[1] in guess:
        return 10
    return 0

if __name__ == "__main__":
    turns = int(input('Enter how many times you want to play: '))
    money = 0
    while turns:
        n = str(random.randint(1, 99))
        guess = input('what is your guess: ')
        money = money + check(n, guess)
        print("Number was",n)
        turns = turns-1
    print("You got ",money,"RS")
