def main():
    a, b = 1, 1
    total = 0
    while a <= 4000000:
        if a%2 == 0:
            total += a
        a, b = b, a+b

    print('The total is: ', total)
        

if __name__ == "__main__":
    main()