import random;

chances=1
number=random.randrange(1,10)
print('Try a wild guess (between 1 and 9)')
guess=int(input('Enter your guess:- '))

while chances<5:
    print(chances)
    if (guess-1==number):
        print('You are very close to the number')
        chances+=1
        guess=int(input('Enter your guess:- '))

    elif (guess+1==number):
        print('You are very close to the number')
        chances+=1
        guess=int(input('Enter your guess:- '))

    elif (guess>number):
        print('Your Guess is too high: Guess a number lower than ',guess)
        chances+=1
        guess=int(input('Enter your guess:- '))

    elif (guess<number):
        print('Your Guess is too low: Gues a number higher than ',guess)
        chances+=1
        guess=int(input('Enter your guess:- '))
    
    else :
        print('Congratulations! You Won!!!')
        break

if not chances<5:
    print('You Lose!!! The number is ', number)