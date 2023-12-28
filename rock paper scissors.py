import random
def game():
    user=input("SELECT BETWEEN THE ROCK OR PAPER OR SCISSORS :  ").upper()
    computer=random.choice(["ROCK","PAPER","SCISSORS"])
    if user==computer:
        print(f"OPPONENT HAS SELECTED THE {computer}")
        return "TIE ! "
    if is_user(user,computer):
        print(f"OPPONENT HAS SELECTED THE {computer}")
        return "YOU WON!"
    print(f"OPPONENT HAS SELECTED THE {computer}")
    return "YOU LOOSE"
def is_user(p,o):
    if (p=="ROCK" and o=="SCISSORS") or (p=="PAPER" and o=="ROCK") or (p=="SCISSORS" and o=="PAPER"):
        return True
print (game())







