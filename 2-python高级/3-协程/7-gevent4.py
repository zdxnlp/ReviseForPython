"""
gevent 提供了协程级的同步原语，用法与标准库类似，但不会阻塞线程：
    1. gevent.lock.Lock：互斥锁，保证协程间的临界区互斥访问。
    2. gevent.event.Event：事件通知，一个协程发信号，其他协程等待。
    3. gevent.semaphore.Semaphore：信号量，控制并发数量。
"""

# 用 Semaphore 控制并发数

from gevent import monkey; monkey.patch_all()
import gevent
from gevent.pool import Pool  # 更简单的并发控制方式

def task(n):
    print(f"任务 {n} 开始")
    gevent.sleep(1)
    print(f"任务 {n} 完成")

# 方式1：用 Semaphore
sem = gevent.lock.Semaphore(2)  # 最多2个协程并发
def task_with_sem(n):
    with sem:
        task(n)
jobs = [gevent.spawn(task_with_sem, i) for i in range(5)]
gevent.joinall(jobs)

# 方式2：用 Pool（更推荐）
print("\n--- 使用 Pool ---")
pool = Pool(2)  # 池大小为2
pool.map(task, range(5))  # 自动控制并发