def main():


    my_list = []

    in_num = input('enter numbers and q for exit')

    while in_num != 'q':
        my_list.append(int(in_num))
        in_num = input('enter numbers and q for exit')

    my_list.sort()
    print(my_list)

    for i in my_list:
        print(i)

main()