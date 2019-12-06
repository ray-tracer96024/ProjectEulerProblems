def main():
    n = 1000000

    while(n != 1):
        if(n%2 == 0):
            n //= 2
            print('Even: ', n)
        else:
            n = 3*n+1
            print('Odd:  ', n)

if __name__ == '__main__':
    main()
