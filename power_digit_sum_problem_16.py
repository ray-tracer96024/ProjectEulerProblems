def pow_dig_sum(n):
    pow = list(str(n))
    return sum([int(i) for i in pow])

def main():
    n = 2 ** 1000
    print("The sum is ", pow_dig_sum(n))

if __name__ == '__main__':
    main()
