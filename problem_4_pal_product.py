# import math

# def reverseNumber(number):
#    return(int(number != 0) and ((number % 10) * (10 ** int(math.log(number, 10))) + reverseNumber(number // 10))) 

def main():
    largestPalindromeProduct = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            if i*j > largestPalindromeProduct:
                if str(i*j)[::-1] == str(i*j):
                    largestPalindromeProduct = i*j
                    break
                else:
                    continue
            break
    print('The largest palindrome product is: ', largestPalindromeProduct)
               

if __name__ == "__main__":
    main()