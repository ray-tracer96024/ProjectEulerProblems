def main():
    pandigital_products = set()
    check_if = set('123456789')

    for i in range(9):
        for j in range(999, 9999):
            s = str(i) + str(j) + str(i*j)
            if len(s) == 9 and set(s) == check_if:
                pandigital_products.add(i*j)
            elif len(s) > 9: break

    for i in range(9, 99):
        for j in range(99, 999):
            s = str(i) + str(j) + str(i*j)
            if len(s) == 9 and set(s) == check_if:
                pandigital_products.add(i*j)
            elif len(s) > 9: break

    print('Answer: ', sum(pandigital_products))


if __name__ == "__main__":
    main()
