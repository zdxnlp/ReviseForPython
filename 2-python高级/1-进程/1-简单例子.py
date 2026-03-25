import multiprocessing
import time

def task(name):
    print(f'进程{name}开始执行')
    time.sleep(2)
    print(f'进程{name}执行完毕')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task, args=('A',))
    p2 = multiprocessing.Process(target=task, args=('B',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('所有进程执行完毕')
