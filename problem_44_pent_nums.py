def is_pentagonal_number(n):
    if ((((24*n) + 1)**0.5)+1)%6 == 0:
        return True
    return False

# def generate_pentagonal_numbers(n, array_of_nums):
#     for i in range(n+1):
#         array_of_nums.append(int(i*((3*i)-1)/2))
#     return array_of_nums

def main():
    # n = 15
    # array_of_nums = []
    # print('The series of pentagonal numbers up to {} is: {}'.format(n, generate_pentagonal_numbers(n, array_of_nums)))

    flag = True
    i = 1
    while flag:
        for j in range(1, i):
            num1 = i*((3*i)-1)/2
            num2 = j*((3*j)-1)/2
            if is_pentagonal_number(num1 + num2) and is_pentagonal_number(num1 - num2):
                print(int(num1-num2))
                flag = False
                break 
        i += 1

if __name__ == '__main__':
    main()