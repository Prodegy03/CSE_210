import random
from jumper import jumper

class word:
    """The word to guess. 
    
     
    
    Attributes:
        _word (str): The word to guess from a specific list.
        _correct (List[word]): correct letters in a word.
    """
  
    def get_random_word(word_list):
     
     wordIndex = random.randint(0, len(word_list) - 1)
     return word_list[wordIndex]

    def displayBoard(missedLetters, correctLetters, secretWord, jumper_PICS):
     print(jumper_PICS[len(missedLetters)])
     print()

     print('Missed letters:', end=' ')
     for letter in missedLetters:
         print(letter, end=' ')
     print()

     blanks = '_' * len(secretWord)

     for i in range(len(secretWord)): 
         if secretWord[i] in correctLetters:
             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

     for letter in blanks:
         print(letter, end=' ')
    print()

    def getGuess(alreadyGuessed):
     # Returns the letter the player entered. This function makes sure the
       # player entered a single letter and not something else.
     while True:
         print('Guess a letter.')
         guess = input()
         guess = guess.lower()
         if len(guess) != 1:
             print('Please enter a single letter.')
         elif guess in alreadyGuessed:
              print('You have already guessed that letter. Choose again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              print('Please enter a LETTER.')
         else:
              return guess
 
    def playAgain():
     # This function returns True if the player wants to play again;
         #  otherwise, it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')

def game(word_list, displayBoard, getGuess,jumper_PICS,get_random_word, playAgain, words ):
    print('JUMP')
    missedLetters = ''
    correctLetters = ''
    secretWord =  get_random_word(word_list)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

     # Let the player enter a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

         # Check if the player has won.
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord +
                '"! You have won!')
                gameIsDone = True
            else:
                missedLetters = missedLetters + guess
         # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(jumper_PICS) - 1:
             displayBoard(missedLetters, correctLetters, secretWord)
             print('You have run out of guesses!\nAfter ' +
                str(len(missedLetters)) + ' missed guesses and ' +
                str(len(correctLetters)) +  'correct guesses, the word was' '"'
                + secretWord + '"')
             gameIsDone = True
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = get_random_word(words)
            else:
                break
            