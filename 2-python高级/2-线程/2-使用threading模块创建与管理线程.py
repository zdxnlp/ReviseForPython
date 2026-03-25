import threading
import time

def call_api(api_name):
    print(f'线程{threading.current_thread().name}开始调用{api_name}')
    time.sleep(1)
    print(f'线程{threading.current_thread().name}调用{api_name}完成')
    return f'{api_name}响应成功'

if __name__ == '__main__':
    start_time = time.time()
    api_list = ["用户接口", "订单接口", "商品接口", "支付接口"]
    threads = []

    # 创建线程
    for api in api_list:
        t = threading.Thread(target=call_api, args=(api,), name=f'API调用线程{api}')
        threads.append(t)

    # 批量启动线程
    for t in threads:
        t.start()

    # 等待所有线程执行完成
    for t in threads:
        t.join()

    print(f'全部接口调用完成，总耗时：{time.time() - start_time:.2f}s')