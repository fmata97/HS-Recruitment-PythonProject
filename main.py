# Fábio Mata - 102802

from SlotMachine import *

# the game itself

slotMachine = SlotMachine()
end = False

while True:
    if end:
        break
        
    slotMachine.play()
    if slotMachine.balance == 0:
        print("Game over! No credit$ left...")
        break
    while True:
        answer = input("Do you want to keep playing? (y/n)")
        if answer == "n":
            end = True
            print("\nUntil next time!")
            break
        elif answer == "y":
            break