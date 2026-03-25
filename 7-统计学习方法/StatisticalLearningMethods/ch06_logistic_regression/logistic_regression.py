import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. 自行实现逻辑斯谛回归 (Self-implemented Logistic Regression)
# ==========================================
class MyLogisticRegression:
    def __init__(self, learning_rate=0.01, max_iter=1000):
        self.lr = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def _sigmoid(self, x):
        # 截断以防止溢出 (exp(-x) 可能很大)
        x = np.clip(x, -250, 250)
        return 1 / (1 + np.exp(-x))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # 梯度下降 (Batch Gradient Descent)
        for _ in range(self.max_iter):
            # 线性模型: z = w*x + b
            linear_model = np.dot(X, self.weights) + self.bias
            # 预测概率: y_pred = sigmoid(z)
            y_pred = self._sigmoid(linear_model)

            # 计算梯度
            # 交叉熵损失的梯度推导结果为: (y_pred - y) * X
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # 更新参数
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = self._sigmoid(linear_model)
        # 将概率转为二分类标签 0 或 1
        class_pred = [1 if p > 0.5 else 0 for p in y_pred]
        return np.array(class_pred)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试
    my_lr = MyLogisticRegression(learning_rate=0.1, max_iter=1000)
    my_lr.fit(X_train, y_train)
    my_preds = my_lr.predict(X_test)
    print("自定义逻辑斯谛回归准确率:", accuracy_score(y_test, my_preds))
    
    # sklearn实现测试 (默认使用 L2 正则化和 L-BFGS 求解器)
    sk_lr = LogisticRegression(max_iter=1000)
    sk_lr.fit(X_train, y_train)
    sk_preds = sk_lr.predict(X_test)
    print("sklearn逻辑斯谛回归准确率:", accuracy_score(y_test, sk_preds))
