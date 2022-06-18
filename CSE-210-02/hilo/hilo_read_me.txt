

Hilo

Rules
Hilo is played according to the following rules.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

CLASSES
player - bool value, true for a correct guess, false for an incorect guess.
card - cards 1 - 13
points = 300 at start

FUNCTIONS
get_card - random.card
player_guess - h or l
high_low_question - displays the question "Higher, or lower?", and collects user input h or l.
correct_guess - correct displayed player = true returned
incorrect_guess - incorect displayed, player = false returned
replay - displays "Would you like to play again?"
game_over - player.points == 0, "game over" displayed
player_running_points - when player == true points + 100, 
when player false points - 75. 


How did you apply abstraction in your program's design?

abstraction is used to:
-build cards and then use the random mod to get a a random card.
-create a point bank to keep track of the points a player obtains while playing.
-create a function working off of the players guess to determine if the player guessed correctly which card is randomly drawn next.

by: Spencer Christensen, malissandspencer@gmail.com
  