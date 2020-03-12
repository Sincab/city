import random


def get_word():
    words = ['apple', 'city', 'london', 'delphi', 'data', 'python', 'sql']
    rnd = random.choice(words)
    star_list = ['*' for x in rnd]
    star_word = ''.join(star_list)
    return [rnd, star_word, len(rnd)]


def play_again():
    answer = input('Would you like to play again? Answer Yes/No?').lower()
    if answer == 'yes' or answer == 'y':
        main()
    else:
        pass

def main():
    actual_word, actual_stared, actual_character = get_word()
    try_life = 10  # int(actual_character * 1.5) not a good idea! long word allows user to enter whole alph!
    print(f'Lets play Hangman! The word contains {actual_character} letters: {actual_stared}')
    letters_guessed = []
    guessed = False
    message = f'(HangmanGame) Enter a letter in word {actual_stared} or a word with {actual_character} character > '
    while guessed == False and try_life > 0:
        print(f'You have {try_life} tries!')
        guess = input(f'(HangmanGame) Enter a letter in word {actual_stared} or a word with {actual_character} character > ')
        #if user enters only 1 letter
        if len(guess) == 1 and guess in letters_guessed:
            print('you have already guessed that letter!')
        elif len(guess) == 1 and guess in actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Well done it is in the word')
        elif len(guess) == 1 and guess not in actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Sorry it is NOT in the word')
        elif len(guess) != 1 and guess != actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Sorry it is not that word!')
        elif guess == actual_word:
            print(f'Well done! {actual_word} is the word! you WON!')
            guessed = True
        else:
            print('Sorry something went wrong, re-start the game')

        status = ''
        if guessed == False:
            for letter in actual_word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == actual_word:
            print('Well done you won')
            guessed = True
        elif try_life == 0:
            print('You have run out of tries before guessing the word')

    play_again()

main()