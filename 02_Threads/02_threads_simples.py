import threading  # 1
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))  # 2

    th.start()

    print('Podemos fazer outras coisas enquanto a thread vai executando...')
    print('Dlc Tecnologia' * 2)

    th.join()

    print('Pronto!')


def contar(o_que, numero):
    for i in range(1, numero + 1):
        print(f'{i} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
