import random
def guess(x):
    random_num=random.randint(1,x)
    guess =0
    higher_hint_count =0
    lower_hint_count =0
    
    while guess!=random_num:
        guess=int(input(f"GUESS THE NO. BETWEEN 1 AND {x} : "))
        if guess>random_num:
            
            print("UMM! YOU HAVE SELECTED THE NUMBER WHICH IS HIGHERN THAN RANDOM ONE")
            higher_hint_count += 1
            print("IF YOU WANT A HINT WRITE YES AND IF NOT WRITE NO")
            intz=input().upper()
            if intz=="YES":
                print(f"MAYBE YOU CAN SUBTRACT THE NO. WITH {guess} AND THEN ADD THE NO. WITH {random_num}")
            else:
                print(f"SO NOW THINK ABOUT THE NO. WHICH IS LESS THAN {guess}")
                
        elif guess<random_num:
            print("UMM! YOU HAVE SELECTED THE NUMBER WHICH IS LOWER THAN RANDOM ONE")
            lower_hint_count+=1
            print("IF YOU WANT A HINT WRITE YES AND IF NOT WRITE NO ! ")
            intz=input()
            if intz=="YES":
                print(f"MAYBE YOU CAN SUBTRACT THE NO. WITH {guess} AND THEN ADD THE NO. WITH {random_num}")
            else:
                print(f"SO NOW THINK ABOUT THE NO. WHICH IS HIGHER THAN {guess}")
                

    total=higher_hint_count+lower_hint_count
    if total==0:
        print("BRAVO! I MEAN MIND BLOWING ! YOU HAVE GUESSED IN THE FIRST GO .")
    elif total==1:
        print("EXCELLENT! YOU HAVE GUESSED IN THE SECOND GO.....")
    elif total==2:
        print("VERY GOOD! YOU HAVE GUESSED IN THE THIRD GO......")
    elif total==3:
        print("GOOD! YOU HAVE GUESSED IN THE FOURTH GO.....")
    else:
        print(f"YOU HAVE GUESSED THE CORRECT NUMBER {random_num} in {total} chance")
    
    
guess(10)
