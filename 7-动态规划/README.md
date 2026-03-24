# Dynamic Programming Study Project

这个项目按常见动态规划类型来组织内容，适合系统复习 LeetCode 中的 DP 题型。

## 目录结构

- `01_linear_dp`：线性 DP
- `02_two_dimensional_dp`：二维 DP
- `03_knapsack_dp`：背包 DP
- `04_interval_dp`：区间 DP
- `05_state_machine_dp`：状态机 DP

## 每道题的学习方式

每道题都配有两个文件：

- `*.md`：题意、为什么属于该类 DP、四步法、递推过程、公式、复杂度
- `*.py`：Python 解法，代码中标出求解步骤

## 动态规划四步法

1. 定义状态：`dp` 数组或状态变量表示什么
2. 写转移：当前状态如何由更小状态得到
3. 定义初始化：最小子问题的答案是什么
4. 确定遍历顺序：保证依赖状态先被计算

## 推荐学习顺序

1. 先看 `01_linear_dp`
2. 再学 `02_two_dimensional_dp`
3. 接着掌握 `03_knapsack_dp`
4. 然后进入 `04_interval_dp`
5. 最后学习 `05_state_machine_dp`
