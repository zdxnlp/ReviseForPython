"""
协程函数：用 async def 定义的函数，调用后返回一个协程对象，不会立即执行。
事件循环：协程的调度器，负责注册、调度和执行协程任务。
任务Task：对协程对象的封装，可被事件循环并发调度。
await：用于挂起当前协程，等待IO操作完成，期间让出CPU给其他协程。
"""

# 协程并发执行IO任务：模拟 3 个网络请求（用 asyncio.sleep 模拟 IO 延迟），对比同步执行和协程并发执行的耗时差异。

import asyncio
import time

# 定义协程函数：模拟一个耗时的IO任务
async def fetch_data(task_name:str,delay:float)->str:
    print(f'[任务{task_name}]开始执行，预计耗时{delay}s')
    # 模拟IO操作，await会挂起当前协程
    await asyncio.sleep(delay)
    print(f'[任务{task_name}]执行完成')
    return f'[任务{task_name}的返回数据]'

async def main():
    start_time = time.time()

    # 方式1:同步执行
    result1 = await fetch_data('A',2)
    result2 = await fetch_data('B',1)
    result3 = await fetch_data('C',3)
    endtime = time.time()

    print(f'\n同步执行所有任务完成，总耗时:{endtime - start_time:.2f}s')
    print("任务返回结果：", result1)
    print("任务返回结果：", result2)
    print("任务返回结果：", result3)


    # 方式2:协程并发执行
    tasks = [
        fetch_data('D',2),
        fetch_data('E',1),
        fetch_data('F',3)
    ]
    # 并发执行所有任务，等待全部完成并收集结果
    results = await asyncio.gather(*tasks)

    end_time = time.time()

    print(f'\n并发执行所有任务完成，总耗时:{end_time-endtime:.2f}s')
    print("任务返回结果：", results)

# 运行事件循环
if __name__ == "__main__":
    asyncio.run(main())