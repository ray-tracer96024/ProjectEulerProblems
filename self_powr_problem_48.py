def self_pwr(n):
    s = 0
    for i in range(1, n+1):
        s += (i ** i)
    return s

def main():
    n = 1000
    x = str(self_pwr(n))
    print(x[-10:])

if __name__ == '__main__':
    main()
