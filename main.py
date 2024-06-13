from simple import simpleNum
from encrypt import encry
import os
from decipher import rsa_decode


def main():
    print("Вас приветствует программа Алгоритм шифрования RSA!")
    text = str(input("Введите текст для шифрования: "))
    if len(text) < 1:
        print("Вы не ввели текст!")
    else:
        while True:
            try:
                p = int(input("Введите простое число p: "))
                q = int(input("Введите простое число q: "))
                break
            except ValueError:
                print("Это не число!")
        if simpleNum(p) and simpleNum(q):
            enc_text = encry(text, p, q)
            with open("blocks.txt", "w") as blocks:
                for item in enc_text:
                    blocks.write(item + '\n')
            os.startfile("blocks.txt")
            while True:
                try:
                    d = int(input("Введите число d: "))
                    n = int(input("Введите число n: "))
                    break
                except ValueError:
                    print("Это не число!")
            input_blocks = []
            with open("blocks.txt", "r") as blocks_file:
                for line in blocks_file:
                    input_blocks.append(line.strip())
            result = rsa_decode(input_blocks, d, n)
            print(f"Расшифрованный текст: {result}")
        else:
            print("p и (или) q - не простые числа!")


if __name__ == "__main__":
    main()
