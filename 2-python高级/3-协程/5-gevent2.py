# 使用 gevent.monkey.patch_all() 可一键替换标准库的阻塞函数，必须在导入其他库之前调用。

# 第一步：先打猴子补丁（必须在导入 time、requests 等库之前）
from gevent import monkey
monkey.patch_all()  # 替换 socket、time、threading 等模块

import gevent
import requests  # 同步库，但被 patch 后自动异步化
import time

def fetch(url):
    print(f"开始请求: {url} (时间: {time.ctime()})")
    resp = requests.get(url)  # 原本阻塞，现在自动切换协程
    print(f"请求完成: {url} (状态码: {resp.status_code}, 时间: {time.ctime()})")
    return len(resp.content)

urls = [
    "https://www.baidu.com",
    "https://www.sina.com.cn",
    "https://www.qq.com"
]

# 并发执行
start = time.time()
jobs = [gevent.spawn(fetch, url) for url in urls]
gevent.joinall(jobs)
end = time.time()

print(f"\n总耗时: {end - start:.2f} 秒")

"""
requests 是同步库，但被 monkey.patch_all() 替换了底层的 socket 调用，因此会自动异步化。
总耗时由最长的请求决定，远低于串行执行的时间。
"""