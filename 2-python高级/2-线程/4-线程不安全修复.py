import threading
import time


counter = 0
lock = threading.Lock()

THREADS = 20
ITERATIONS = 1000


def unsafe_add():
    global counter
    for _ in range(ITERATIONS):
        # 故意把“读”和“写”拆开，放大竞态条件
        current = counter
        time.sleep(0.0001)
        counter = current + 1


def safe_add():
    global counter
    for _ in range(ITERATIONS):
        with lock:
            current = counter
            time.sleep(0.0001)
            counter = current + 1


def run_demo(target):
    global counter
    counter = 0
    threads = [threading.Thread(target=target) for _ in range(THREADS)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return counter


if __name__ == "__main__":
    expected = THREADS * ITERATIONS

    unsafe_result = run_demo(unsafe_add)
    print(f"不加锁  预期: {expected}, 实际: {unsafe_result}")

    safe_result = run_demo(safe_add)
    print(f"加锁后  预期: {expected}, 实际: {safe_result}")