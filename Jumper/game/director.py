from t_s import TerminalService
from hider import word



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
   """
    def __init__(self, jumper):
         """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
         self._word = word()
         self._is_playing = True
         self._jumper = jumper()
         self._t_s = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_word = self._terminal_service.guess_letter("\nEnter Letter: ")