def pythagoras_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if((a**2 + b**2) == c**2):
                return a*b*c

print(pythagoras_triplet())
