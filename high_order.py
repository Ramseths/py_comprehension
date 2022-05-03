from functools import reduce


def run():
    my_list = [1,2,3,4,5]
    squares = list(map(lambda x: x**2,my_list))
    print(squares)

    my_second_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_second_list)
    print(all_multiplied)


if __name__ == '__main__':
    run()