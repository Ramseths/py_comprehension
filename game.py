import random
import os

def get_word():
    words = []
    with open('./files/data.txt','r',encoding='utf-8') as f:
        words = [i for i in f]
    return words
            
def game(word):
    print('¡Adivina la palabra!')
    text =  ' _ ' * (len(word) - 1)
    win = False
    counter = 0
    while win == False:
        print(text)
        print(word)
        current = input('Ingresa una letra: ').upper()
        for i, n in enumerate(word):
            print(f'{i} {n}')
            if n == current:
                text[i] = current
                counter += 1
        
        if counter == len(word):
            win = True
        os.system("cls")
    os.system("cls")
    print(f'Ganaste! La palabra era {word}')

def run():
    size = get_word()
    number = random.randint(1, len(size) - 1)
    word = size[number]
    word = word.upper()
    game(word)

if __name__ == '__main__':
    run()