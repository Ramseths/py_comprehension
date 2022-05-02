def run():
    my_list = [0, "Hello", True, 4.5]
    my_dict = {"firstName":"Jesus","lastName":"Echeverria"}

    super_list = [
        {"firstName":"John","lastName":"Mc"},
        {"firstName":"Ram","lastName":"Echeverria"},
        {"firstName":"Jose","lastName":"Rivera"},
    ]

    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[1, -2, 4, -5],
        "floating_nums":[1.1, 2.2, 3.3, 4.4]
    }


    # Print content
    for key, value in super_dict.items():
        print(f'{key} - {value}')

    print_list(super_list)

def print_list(input):
    for i in input:
        for key, value in i.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()