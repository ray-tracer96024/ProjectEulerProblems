def main():
    largest = 0
    for i in range(1, 10000):
        mult = ''
        counter = 1
        while(len(mult) < 9):
            mult += str(i*counter)
            counter += 1

        if(((len(mult)) == 9) and ((len(set(mult))) == 9) and ('0' not in mult)):
            if(int(mult) > largest):
                largest = int(mult)
    print('Answer: ', largest)

if __name__ == "__main__":
    main()