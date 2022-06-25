import random

class jumper:
    """The person looking for the Hider . 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
        distance (List[int]): The distances travelled.
    """
   
    word_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar",
      "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk",
       "lion","lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl", "panda",
       "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep",
       "skunk", "sloth", "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle",
       "weasel", "whale", "wolf", "wombat", "zebra"]
            
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