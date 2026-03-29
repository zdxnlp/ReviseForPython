import threading
import time

class DataSyncThread(threading.Thread):
    def __init__(self,data_type,sync_interval, name):
        super().__init__() # 必须调用父类构造方法
        self.data_type = data_type
        self.sync_interval = sync_interval
        self.name = name
        self.is_running = True # 线程运行控制标志

    # 重写run方法，线程启动后执行的核心逻辑
    def run(self):
        while self.is_running:
            print(f'线程{self.name}开始同步{self.data_type}数据')
            time.sleep(self.sync_interval) # 模拟同步IO耗时
            print(f'线程{self.name}同步{self.data_type}数据完成')

    # 自定义停止方法
    def stop(self):
        self.is_running = False
        print(f'线程{self.name}收到停止信号，即将退出')

if __name__ == '__main__':
    # 创建线程实例
    user_sync_thread = DataSyncThread(data_type="用户", sync_interval=2, name="用户同步线程")
    order_sync_thread = DataSyncThread(data_type="订单", sync_interval=3, name="订单同步线程")

    # 启动线程
    user_sync_thread.start()
    order_sync_thread.start()

    # 主线程等待10秒后停止子线程
    time.sleep(10)
    user_sync_thread.stop()
    order_sync_thread.stop()

    # 等待线程优雅退出
    user_sync_thread.join()
    order_sync_thread.join()
    print("所有数据同步线程已退出")