import math

def main():
    n = 600851475143
    while n%2 == 0:
        print(2, )
        n /= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            print(i, end = ' ')
            n /= i

    if n>2:
        print(n)

    print()

if __name__ == "__main__":
    main()