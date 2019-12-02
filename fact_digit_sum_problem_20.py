def factorial(n):
    if n<0:
        return -1
    elif(n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def get_sum(n):
	sum = 0
	while (n != 0):
		sum = sum + int(n % 10)
		n = int(n/10)
	return sum

def main():
    n = 100
    x = factorial(n)
    print("The factorial of ", n, " is: ", x)
    store_x = x
    y = get_sum(store_x)
    print("The sum of the digits is: ", y)

if __name__ == '__main__':
    main()
