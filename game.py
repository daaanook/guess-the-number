import random

levels = {
    "1": ("easy", 50, 10),
    "2": ("medium", 100, 7),
    "3": ("hard", 500, 9),
}

best_score = None


def get_level():
    print("Choose level:")
    print("1 - easy (1-50, 10 tries)")
    print("2 - medium (1-100, 7 tries)")
    print("3 - hard (1-500, 9 tries)")

    lvl = input("> ")
    while lvl not in levels:
        print("no such level, try again")
        lvl = input("> ")
    return levels[lvl]


def get_number(max_num):
    while True:
        n = input("your guess: ")
        if not n.isdigit():
            print("that's not a number")
            continue
        n = int(n)
        if n < 1 or n > max_num:
            print("number should be between 1 and", max_num)
            continue
        return n


def play():
    name, max_num, tries = get_level()
    secret = random.randint(1, max_num)

    print()
    print("Level:", name)
    print("I picked a number from 1 to", max_num, "- you have", tries, "tries")

    used = 0
    while used < tries:
        guess = get_number(max_num)
        used += 1

        if guess == secret:
            print("You got it! Tries used:", used)
            return used
        elif guess < secret:
            print("higher")
        else:
            print("lower")

        print("tries left:", tries - used)

    print("No more tries :( The number was", secret)
    return None


while True:
    result = play()

    if result != None:
        if best_score == None or result < best_score:
            best_score = result
            print("New best score!")

    if best_score != None:
        print("Best score:", best_score)

    answer = input("\nPlay again? (y/n) ").lower()
    if answer != "y" and answer != "yes":
        print("bye!")
        break
