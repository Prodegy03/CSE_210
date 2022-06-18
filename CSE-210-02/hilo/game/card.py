from msilib.schema import Class
import random

class Cards:
    def __init__(self):
        self.value = 0
        self.points = 0

    def Card(self):
        self.value = random.randint(1, 13)
        
    def prev_card_value(self):
        prev_card = card;