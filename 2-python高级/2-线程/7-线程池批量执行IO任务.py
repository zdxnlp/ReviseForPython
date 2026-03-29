import threading
from concurrent.futures import ThreadPoolExecutor
import time
import os

# 模拟全栈业务：批量处理文件（IO密集型）
def process_file(file_name):
    print(f"线程ID：{os.getpid()}-{threading.get_ident()} 开始处理：{file_name}")
    time.sleep(0.5)  # 模拟文件读写IO耗时
    print(f"处理完成：{file_name}")
    return f"{file_name} 处理结果"

if __name__ == '__main__':
    start_time = time.time()
    file_list = [f"文件_{i}.txt" for i in range(20)]

    # 创建线程池，最大线程数10
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 批量提交任务，map方法按顺序返回结果
        results = executor.map(process_file, file_list)

    # 输出所有结果
    print("-"*50)
    print("所有任务处理完成，结果如下：")
    for res in results:
        print(res)

    print(f"总耗时：{time.time() - start_time:.2f}秒")
    # 预期结果：耗时约1秒（20个任务，10个并发，2轮执行）