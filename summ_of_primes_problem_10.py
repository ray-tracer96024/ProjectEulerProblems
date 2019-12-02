def sieve_of_eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def main():
    n = 2000000
    print(sum(list(sieve_of_eratosthenes(n))))

if __name__ == '__main__':
    main()
