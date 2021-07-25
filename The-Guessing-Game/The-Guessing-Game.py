from random import randint

num = randint(1,100)
guess_list = [0] # Guess list containing a 0 flag (as False)

print("""Welcome to THE GUESSING GAME\n 
Guidelines:
1. The system picks a random number between 0 and 100.
2. If your guess is more than 10 away from my number, I'll tell you you're COLD.
3. If your guess is within 10 of my number, I'll tell you you're WARM.
4. If your guess is farther than your most recent guess, I'll say you're getting COLDER.
5. If your guess is closer than your most recent guess, I'll say you're getting WARMER.\n
LET'S GO!!!""")

while True:
    
    guess = int(input('\nEnter your Guess: '))
    
    if guess < 1 and guess > 100:
        print('OUT OF BOUNDS!')
        break
    
    if guess == num:
        print(f'\nCONGRATULATIONS!!!\n\nYou guessed it in just {len(guess_list)} guesses.')
        break
        
    #Add the guessed word to the list of guesses    
    guess_list.append(guess)
    
    #Guess_list[-2] = 0 indicates False i.e. it has more than two guesses
    if guess_list[-2]:
        if abs(num-guess) < abs(num-guess_list[-2]):
            print('WARMER')
        else:
            print('COLDER')
    
    #This block gets executed when guess_list[-2] is true.
    else:
        if abs(num-guess) <= 10:
            print('WARM')
        else:
            print('COLD')