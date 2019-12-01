def sum_of_square(n):
    s = 0
    for i in range(1, n+1):
        s += (i ** 2)
    print(s, end = ' ')
    return s

def square_of_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    s = s ** 2
    print(s, end = ' ')
    return s

def main():
    n = 100
    diff = 0
    diff = square_of_sum(n) - sum_of_square(n)
    print(diff)

if __name__ == '__main__':
    main()
