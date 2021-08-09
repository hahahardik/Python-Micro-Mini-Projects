# Takes the user guess
def user_guess():
    
    guess = input("Enter your guess: ")
    return guess


# Checks the guess entered by the user
# For simplicity purposes, secret value has beeen fixed
import random
sv = random.randint(1000, 9999)

def check_guess(guess,secret_value = sv):

    
    list_sv = [int(i) for i in str(secret_value)]
    list_guess = [int(i) for i in str(guess)]
    
    
    gc_cp = 0    # Guessed correctly and at correct position
    gc_wp = 0    # Guessed correctly but at wrong position
    
    for i in list_guess:
        if i in list_sv:
            if list_sv.index(i) == list_guess.index(i):
                gc_cp += 1
            else:
                gc_wp += 1
        else:
            continue
            
        
    return f'{gc_cp}-{gc_wp}'


# Checks if the guess is correct and declares win
def win_check(r):
    
    if r == '4-0':
        print('\nYayy!!! You guessed it right.')
        return True
    else:
        pass


# Asks if the user wants to continue or not
def resume_play():
    
    resume = input('\nDo you want to continue: ')
    if resume.lower().startswith('y'):
        return True
    elif resume.lower().startswith('n'):
        return False
    else:
        print('Enter a valid statement.')
        resume_play()


# Final Game
def mastermind():
    
    print('How Good are you at guessing?\n')
    print('Welcome to the MASTERMIND!!! \n')
    
    global flag
    flag = True
    
    i = 1  
    
    while flag:
        
        if i%5 == 0:
            flag = resume_play()
            if flag:
                guess = user_guess()
                r = check_guess(guess)
                print(r)
                if win_check(r):
                    print('\nThank You for playing!')
                    break
                else:
                    i += 1
            else:
                print('\nThank You for playing!')
            
        else :
            guess = user_guess()
            r = check_guess(guess)
            print(r)
            if win_check(r):
                print('\nThank You for playing!')
                break
            else:
                i += 1