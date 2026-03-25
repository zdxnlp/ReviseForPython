# 由于进程内存空间独立，必须掌握如何在进程间传递数据
"""
常用方式：
    1. Queue：先进先出队列，常用于生产者-消费者模型，进程安全
    2. Pipe：管道，用于两个进程之间的双向通信
    3. Manager：更高级的管理器，可以在进程间共享列表、字典等
"""

# 使用Queue传递数据
import multiprocessing

def producer(q):
    """生产者：往队列里放数据"""
    for item in ['数据A','数据B','数据C']:
        print(f'生产了：{item}')
        q.put(item)

def consumer(q):
    """消费者：从队列里取数据"""
    while True:
        item = q.get()
        if item is None:
            break
        print(f'消费了：{item}')

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p_prod = multiprocessing.Process(target=producer, args=(q,))
    p_cons = multiprocessing.Process(target=consumer, args=(q,))

    p_prod.start()
    p_cons.start()

    p_prod.join()
    q.put(None) # 发送结束信号
    p_cons.join()