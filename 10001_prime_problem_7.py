def ten_thousand_one_prnos(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if prime[p] == True:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = True
    for i in range(n + 1):
        if prime[p]:
            print(p)

def main():
    n = 10001
    ten_thousand_one_prnos(n)

if __name__ == '__main__':
    main()
