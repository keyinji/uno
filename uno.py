import random

colours = ("Red", "Yellow", "Blue", "Green")

ranks = list(range(1,11)) # declarative way

deck = [(rank, colour) for rank in ranks for colour in colours]

random.shuffle(deck)

print(deck)

def start_game(deck):
    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck[14:]
    # p1 = [deck.pop(0) for _ in range(7)] works too
    face_up = deck.pop(0)
    main_loop(p1, p2, face_up, deck)

def main_loop(p1, p2, face_up, deck):
    current = 0
    while len(p1) > 0 and len(p2):
        print(f"It is the player {current + 1}'s turn")
        print(f"The face up card is {face_up}")
        print(f"Player {current+1}'s hand is {p1}")

        # Pick or play a card
        pick_option = int(input("Choose 1 to play and 2 to draw a card: "))
        if pick_option == 1: #user wants to play
            index = int(input("What card do you want to play (starting at 1): ")) - 1
            if p1[index][0] == face_up[0] or p1[index][1] == face_up[1]:
                face_up = p1.pop(index)


        else:
            p1.append(deck.pop(0))
        p1, p2 = p2, p1
        current = (current + 1) % 2


###
# +2 
# make one change to the code, as in, add one feature
# black cards 
# 4 players 