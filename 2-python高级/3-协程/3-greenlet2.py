# 传递参数与返回值：switch() 可传递参数（作为目标协程的输入），并接收目标协程的返回值。
from greenlet import greenlet


def calculator():
    # 接收主 greenlet 传来的参数
    a, b = gr_parent.switch()
    print(f"Calculator: 收到参数 {a}, {b}")

    # 计算结果并返回给主 greenlet
    result = a + b
    gr_parent.switch(result)


# 创建子 greenlet，显式指定父协程为当前主 greenlet
gr_parent = greenlet.getcurrent()  # 获取当前协程（主 greenlet）
gr_calc = greenlet(calculator, parent=gr_parent)

print("主 greenlet: 启动 calculator")
gr_calc.switch()

# 第一次切换：传递参数 3 和 5 给 calculator
print("主 greenlet: 发送参数 3, 5")
gr_calc.switch(3, 5)

# 第二次切换：接收 calculator 的返回值
print("主 greenlet: 等待结果...")
result = gr_calc.switch()
print(f"主 greenlet: 收到结果 {result}")
