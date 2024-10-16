import random

colours = ("Red", "Yellow", "Blue", "Green")

ranks = list(range(1,11)) # declarative way

deck = [(rank, colour) for rank in ranks for colour in colours]