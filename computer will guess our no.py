import random
def computer_guess(x):
    low=1
    high=x
    user_feedback=""
    while user_feedback!="c":
        random_num=random.randint(low,high)
        user_feedback=input(f"MY GUESS NO. IS : {random_num} PLEASE HELP ME AND TELL IF, MY GUESS IS HIGHER VALUE THAN WRITE 'H' IF LOW THAN WRITE 'L' IF CORRECT WRITE 'C' :  ").lower()
        if user_feedback=="h":
            high=random_num-1
        elif user_feedback=="l":
            low=random_num+1
    print(f"COMPUTER HAS GUESSED IT CORRECTLY , THE NUMBER IS {random_num}")
computer_guess(10)




