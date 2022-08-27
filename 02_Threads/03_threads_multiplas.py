import threading
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('burado', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12))
    ]

    # adiciona a thread na pool de threads para pronto.  #3
    [th.start() for th in threads]

    print('Podemos fazer outras coisa enquanto a thread vai executando...')
    print('Dlc Tecnologia' * 2)

    # avisa para ficar aguardando aqui até athread terminar a execução  #4
    [th.join() for th in threads]

    print('Pronto!')


def contar(o_que, numero):
    for i in range(1, numero + 1):
        print(f'{i} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
