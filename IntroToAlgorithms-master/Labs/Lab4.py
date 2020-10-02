""" Guessing Game """
import random


def guessing_game():
    x = [1, 1000]   # default range
    answer = random.randint(min(x), max(x))  # generate a random integer in the range
    get_range(x, answer)
    guess_count = 0     # count only when the input is valid
    ex_str = "ex"
    print(f"== Enter '{ex_str}' to stop running. ==")
    while True:
        inp = input(f"Enter your guess from {min(x)} to {max(x)}: ")
        if inp.lower() == ex_str:
            break
        try:
            if int(inp) == answer:
                guess_count += 1
                print(f"You got it! The hidden number is {answer}")
                print(f"It took you {guess_count} guess(es).")
                break
            elif int(inp) < min(x) or max(x) < int(inp):
                print("Please enter a number between the range.")
            else:
                guess_count += 1
                print(f"Wrong! Guess count: {guess_count}")
                get_range(x, answer)
        except ValueError:
            print("Please enter a number.")
        except:
            print("Try again!")
    pass

def get_range(x, answer):
    random1 = random.randint(min(x), answer)
    random2 = random.randint(answer, max(x))
    x[0] = min(random1, random2)
    x[1] = max(random1, random2)
    pass

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()