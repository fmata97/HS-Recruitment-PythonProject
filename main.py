# Fábio Mata - 102802

from SlotMachine import *

# the game itself

slotMachine = SlotMachine()

while True:
    slotMachine.play()
    if slotMachine.balance == 0:
        print("Game over! No credit$ left...")
        break
    answer = input("Do you want to keep playing? (y/n)")
    if answer == "n":
        break