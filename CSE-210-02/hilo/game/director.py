from game.card import Cards


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            card = Card()
            self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        
        pick_card = input("Higher or Lower (H/L) ")
        pick_card.lower = pick_card
        high = (pick_card == "h")
        low = (pick_card == "l")
        new_card = input("Play Again [y/n] ")
        self.is_playing = (new_card == "y")
    def check_inputs(Card):
        card = Card()
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
           return 

        for i in range(len(self.cards)):
            card = self.cards[i]
            card.pick_card()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
           return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "

        print(f"The card is: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)