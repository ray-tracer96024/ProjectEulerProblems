"""
    # Will modify this since the output has not been cross-verified
"""

def factorial(n):
    if(n <= -1):
        return -1
    elif(n == 0):
        return 1
    else:
        return n * factorial(n-1)

def summation(n):
    result = 0
    for i in range(10, 2540161):
        sum_of_facts = 0
        n = i
        while n > 0:
            x = n % 10
            n //= 10
            sum_of_facts += factorial(x)

        if sum_of_facts == i:
            result += i

    return n

def main():
    n = 145
    print(summation(n))

if __name__ == '__main__':
    main()
