def main():
    store_lst = [int(d) for n in range(10**2) for d in str(n)]
    print('The sequence is: ', store_lst, end='\n')

    a = ''

    for i in range(1, 185186):
        a += str(i)
    
    store_1 = int(a[0])
    print('O/p for store_1: ', store_1, end='\n')

    store_10 = int(a[9])
    print('O/p for store_10: ', store_10, end='\n')

    store_100 = int(a[99])
    print('O/p for store_100: ', store_100, end='\n')

    store_1000 = int(a[999])
    print('O/p for store_1000: ', store_1000, end='\n')

    store_10000 = int(a[9999])
    print('O/p for store_10000: ', store_10000, end='\n')

    store_100000 = int(a[99999])
    print('O/p for store_100000: ', store_100000, end='\n')

    store_1000000 = int(a[999999])
    print('O/p for store_1000000: ', store_1000000, end='\n')

    result = store_1 * store_10 * store_100 * store_1000 * store_10000 * store_100000 * store_1000000
    print('Result: ', result, end = '\n')

if __name__ == '__main__':
    main()