# 生产者 - 消费者模型

from gevent import monkey; monkey.patch_all()
import gevent
from gevent.queue import Queue

def producer(q: Queue, name: str):
    """生产者：生成数据并放入队列"""
    for i in range(5):
        item = f"{name}-数据-{i}"
        print(f"[生产者 {name}] 生产: {item}")
        q.put(item)
        gevent.sleep(0.5)  # 模拟生产耗时

def consumer(q: Queue, name: str):
    """消费者：从队列取数据并处理"""
    while True:
        item = q.get()  # 队列为空时自动挂起协程
        print(f"[消费者 {name}] 消费: {item}")
        gevent.sleep(1)  # 模拟消费耗时

# 创建队列
q = Queue(maxsize=3)  # 队列最大长度为3，满时生产者会挂起

# 创建生产者和消费者协程
p1 = gevent.spawn(producer, q, "P1")
p2 = gevent.spawn(producer, q, "P2")
c1 = gevent.spawn(consumer, q, "C1")
c2 = gevent.spawn(consumer, q, "C2")

# 等待生产者完成（消费者是无限循环，这里仅演示）
gevent.joinall([p1, p2])