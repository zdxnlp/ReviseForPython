from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 模拟异步发送短信
def send_sms(phone):
    print(f"开始给{phone}发送短信")
    time.sleep(1)
    if phone.startswith("138"):
        raise Exception(f"给{phone}发送短信失败")
    return f"给{phone}发送短信成功"

# 回调函数：任务完成后自动执行
def sms_callback(future):
    try:
        result = future.result()
        print(f"回调处理：{result}，记录发送日志")
    except Exception as e:
        print(f"回调处理：发送失败，错误信息：{e}，触发重试机制")

if __name__ == '__main__':
    start_time = time.time()
    phone_list = ["13800000001", "13900000002", "13700000003", "13600000004"]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for phone in phone_list:
            # 异步提交任务
            future = executor.submit(send_sms, phone)
            # 绑定回调函数
            future.add_done_callback(sms_callback)
            futures.append(future)

        # 主线程可以继续做其他事情，无需阻塞等待
        print("主线程继续执行其他业务逻辑...")
        time.sleep(2)

        # 等待所有任务完成
        for future in as_completed(futures):
            pass

    print(f"全部任务处理完成，总耗时：{time.time() - start_time:.2f}秒")