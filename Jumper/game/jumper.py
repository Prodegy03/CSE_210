import random

class jumper:
    """The person looking for the Hider . 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
        distance (List[int]): The distances travelled.
    """
   
    word = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar",
      "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk",
       "lion","lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl", "panda",
       "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep",
       "skunk", "sloth", "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle",
       "weasel", "whale", "wolf", "wombat", "zebra"]
            
    def __init__(self, word):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = random.word
        
    def getRandomWord(wordList):
         wordIndex = random.randint(0, len(wordList) - 1)
         return wordList[wordIndex]
        
    def change_word(self, word):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._word =word
    jumper_PICS = ['''
     X
    /|\
    / \ 
   ''', '''

    \ /
     0
    /|\
    / \ ''', '''
   \   /
    \ /
     0
    /|\
    / \ 
   
    ''', '''

     
    ___
   \   /
    \ /
     0
    /|\
    / \ ''', '''
    
   /   \
    ___
   \   /
    \ /
     0
    /|\
    / \ ''', '''
    ___
   /   \
    ___
   \   /
    \ /
     0
    /|\
    / \ ''']