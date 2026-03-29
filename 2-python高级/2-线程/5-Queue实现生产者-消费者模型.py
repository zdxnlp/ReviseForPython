import threading
import queue
import time

# 创建线程安全的队列，最大容量10
task_queue = queue.Queue(maxsize=10)

# 生产者线程：生成任务，放入队列
def producer(name):
    for i in range(5):
        task = f'任务--{name}--i'
        task_queue.put(task)
        print(f'生产者{name}生产了：{task}')
        time.sleep(0.5)
    print(f'生产者{name}生产完成，退出')

# 消费者线程：从队列取出任务，执行处理
def consumer(name):
    while True:
        # 从队列取任务，block=True表示对俄为空时阻塞等待
        task = task_queue.get()
        # 收到结束信号，退出循环
        if task is None:
            print(f"消费者{name} 收到结束信号，退出")
            task_queue.task_done()  # 标记任务处理完成
            break
        # 模拟任务处理
        print(f"消费者{name} 处理了：{task}")
        time.sleep(1)
        task_queue.task_done()  # 标记任务处理完成

if __name__ == '__main__':
    # 创建2个生产者，3个消费者
    producers = [threading.Thread(target=producer, args=(f"P{i}",)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(f"C{i}",)) for i in range(3)]

    # 启动所有线程
    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    # 等待所有生产者生产完成
    for p in producers:
        p.join()

    # 往队列里放入结束信号，数量等于消费者数量
    for _ in range(len(consumers)):
        task_queue.put(None)

    # 等待队列所有任务处理完成
    task_queue.join()
    print("所有任务全部处理完成，程序退出")