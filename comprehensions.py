def run():
    # List comprehension
    my_list = [i ** 2 for i in range(1, 101) if i%3 != 0]
    print(my_list)

    #4, 6 & 9
    second_list = [i for i in range(1, 100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(second_list)

if __name__ == '__main__':
    run()