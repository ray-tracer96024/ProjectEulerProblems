def main():
    raise_to = 5

    summation_of_nos = 0

    for i in range(1, 354294):
        number = i
        temporary = number
        summation = 0 
        while temporary:
            remainder = temporary % 10
            summation += (remainder ** raise_to)
            temporary //= 10

        if number == summation:
            summation_of_nos += summation
            print('{}'.format(summation_of_nos))
        else:
            continue


if __name__ == "__main__":
    main()