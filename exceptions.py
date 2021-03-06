def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input("Ingresa un número: "))
            if num <= 0:
                raise ValueError('Es un número negativo')
            print(divisors(num))
            print('Close')
            break
        except ValueError:
            print('Debes ingresar un número')

if __name__ == '__main__':
    run()