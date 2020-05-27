def tri_nums(n, array):
    for i in range(1, n+1):
        array.append(int((i*(i+1))/2))
    return array

def converter(c):
    return ord(c) - 64

def main():
    n = 26
    array = []
    tri_nums(n, array)
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    dictionary_of_tri_alpha = dict(zip(array, alphabets))
    print('The dictionary is: {}'.format(dictionary_of_tri_alpha))
    
    print('\n')

    line_list = []
    with open('p042_words.txt') as f:
        for line in f:
            line_list.append(line)
    f.close()
    line_list = line.strip().split(',')
    # print('The line list is: {} \nThe size of the line list is: {}'.format(line_list, len(line_list)))

    counter = 0

    for l in line_list:
        x = sum(map(converter, l[1: -1]))
        if(((8*x+1)**0.5) == int(((8*x+1)**0.5))):
            counter += 1

    print('The number of triangle words are: {}'.format(counter))
    
if __name__ == '__main__':
    main()
