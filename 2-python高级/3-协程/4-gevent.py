"""
gevent是一个基于greenlet的高性能异步网络库，底层封装了libev/libuv事件循环。
它的核心设计理念：
    1. 用同步代码的写法，实现异步程序的性能。
    2. 自动处理IO阻塞时的协程切换，无需显示使用async/await语法。
核心依赖：
    1. greenlet：提供用户态轻量级协程，实现协程的创建与切换。
    2. libev/libuv：高性能事件循环库，监听IO事件，驱动协程调度。

核心原理：
    1. 协程调度：greenlet+事件循环
        gevent用greenlet实现协程，但无需手动调用switch()，而是通过事件循环自动调度：
        1. 当协程遇到IO阻塞时，gevent会自动挂起当前协程，切换到其他就绪协程。
        2. 当IO事件就绪，事件循环会唤醒对应的协程继续执行。
        Monkey Patch（猴子补丁）：
        这是gevent最具特色的功能：动态替换python标准库中的阻塞函数为非阻塞版本，让原本的同步代码无需修改即可异步执行。
"""
import gevent

def task(name, delay):
    print(f"[任务 {name}] 开始，延迟 {delay} 秒")
    gevent.sleep(delay)  # 模拟 IO 阻塞，自动切换协程
    print(f"[任务 {name}] 完成")
    return f"任务 {name} 的结果"

# 创建 3 个协程
jobs = [
    gevent.spawn(task, "A", 2),
    gevent.spawn(task, "B", 1),
    gevent.spawn(task, "C", 3)
]

# 等待所有协程完成
gevent.joinall(jobs)

# 获取协程返回值
for job in jobs:
    print(job.get())