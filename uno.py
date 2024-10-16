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
    face_up = deck.pop(0)
    main_loop(p1, p2, face_up, deck)

def main_loop(p1, p2, face_up, deck):
    current = 0
    print(f"It is the player {current + 1}'s turn")
    print(f"The face up card is {face_up}")
    print(f"Player {current+1}'s hand is {p1}")

    # Pick or play a card
    pick_option = int(input("Choose 1 to play and 2 to draw a card"))
    if pick_option == 1: #user wants to play
        index = int(input("What card do you want to play (starting at 1)"))
        index -= 1
        if p1[index][0] == face_up[0] or p1[index][1] == face_up[1]:
            card_to_play = p1.pop(index)


    if pick_option == 2:
        p1.append(deck.pop(0))


