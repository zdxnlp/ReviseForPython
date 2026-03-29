import threading
import time

# 创建信号量，限制最大并发数为3
max_concurrent = threading.Semaphore(3)

# 模拟调用第三方接口
def request_api(api_id):
    # 获取信号量，超过3个线程会阻塞等待
    with max_concurrent:
        print(f"线程 {threading.current_thread().name} 开始调用接口-{api_id}")
        time.sleep(2)  # 模拟接口请求耗时
        print(f"线程 {threading.current_thread().name} 调用接口-{api_id} 完成")

if __name__ == '__main__':
    start_time = time.time()
    # 创建10个线程，同时发起接口请求
    threads = [threading.Thread(target=request_api, args=(i,)) for i in range(10)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"全部接口调用完成，总耗时：{time.time() - start_time:.2f}秒")
    # 预期结果：耗时约8秒（10个任务，3个并发，4轮执行），而非串行的20秒