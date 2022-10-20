# Fábio Mata - 102802

from math import floor
from random import random

# classes and game definitions

symbols = [(),("#", 5),("?", 10),("&", 20),("%", 70),("@", 200),("€", 1000),("$", 100000)]

class SlotMachine:
    def __init__(self):
        self.slot1 = Slot()
        self.slot2 = Slot()
        self.slot3 = Slot()
        self.bet = 0
        while True:
            self.balance = eval(input("Value to deposit: $"))
            if self.balance > 0: break

    def play(self):
        while True:
            self.bet = eval(input("\nPlace your bet: $"))
            if self.bet > self.balance:
                print("You don't have enough money!")
            elif self.bet > 0:
                break
        
        self.balance -= self.bet
        self.rollSlots()
        print(self)
        self.checkWin()
    
    def rollSlots(self):
        self.slot1.roll()
        self.slot2.roll()
        self.slot3.roll()

    def checkWin(self):
        if self.slot1.result == self.slot2.result == self.slot3.result:
            prize = self.bet*symbols[self.slot1.result][1]
            self.balance += prize
            print(f"You won ${prize}! New balance: ${self.balance}")
        else:
            print(f"You lost! Credits left: ${self.balance}")

    def __str__(self):
        return f"{self.slot1}|{self.slot2}|{self.slot3}"


class Slot:
    def __init__(self):
        self.result = 0

    def roll(self):
        n = floor(random()*155 + 1)

        if n < 50:
            self.result = 1
        elif n < 90:
            self.result = 2
        elif n < 120:
            self.result = 3
        elif n < 140:
            self.result = 4
        elif n < 150:
            self.result = 5
        elif n < 155:
            self.result = 6
        else:
            self.result = 7
        
    def __str__(self):
        return symbols[self.result][0]