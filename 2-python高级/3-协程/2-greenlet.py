"""
greenlet是python的一个底层协程库，提供了比asyncio更原始的协程实现。
核心特定：
1. 显示切换：协程的调度完全由程序员通过switch()方法手动控制，而非操作系统或事件循环自动调度。
2. 轻量级：每个greenlet拥有独立的栈，切换时仅需保存/回复栈状态，开销极小。
3. 无内置IO异步：纯greenlet不处理IO阻塞，需手动切换；实际项目中常用gevent（基于greenlet+异步IO库）来实现自动IO切换。
"""

"""
1. 主greenlet：程序启动时默认创建的协程，是所有其他greenlet的“父协程”。
2. 子greenlet：通过greenlet(func)创建的协程，默认父协程是创建他的那个协程。
3. switch()：用于显式切换到目标greenlet，可传递参数/返回值。
"""

# 模拟两个任务交替执行，展示switch()的显式调度
from greenlet import greenlet

def task1():
    print("Task 1: 开始执行")
    # 显式切换到 task2
    gr2.switch()
    print("Task 1: 恢复执行")
    # 再次切换到 task2
    gr2.switch()
    print("Task 1: 执行完毕")

def task2():
    print("Task 2: 开始执行")
    # 切换回 task1
    gr1.switch()
    print("Task 2: 恢复执行")
    # task2 执行完毕，自动切回父协程（主 greenlet）

# 创建子 greenlet（父协程默认是主 greenlet）
gr1 = greenlet(task1)
gr2 = greenlet(task2)

# 从主 greenlet 切换到 gr1
gr1.switch()
print("主 greenlet: 所有任务结束")


