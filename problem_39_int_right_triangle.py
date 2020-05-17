from collections import Counter

def main():
    perimeters = []
    for a in range(1, 500):
        for b in range(1, 500):
            c = ((a**2) + (b**2))**0.5
            if int(c) == c and a+b+c<=1000:
                perimeters.append(a+b+c)

    p = Counter(perimeters)
    print(p.most_common(1)[0])

if __name__ == "__main__":
    main()