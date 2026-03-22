import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# ==========================================
# 1. 自行实现感知机 (Self-implemented Perceptron)
# ==========================================
class MyPerceptron:
    def __init__(self, learning_rate=0.1, max_iter=1000):
        self.lr = learning_rate
        self.max_iter = max_iter
        self.w = None
        self.b = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        
        # 将标签 y 转换为 1 和 -1
        y_ = np.where(y <= 0, -1, 1)
        
        # 随机梯度下降
        for _ in range(self.max_iter):
            for idx, x_i in enumerate(X):
                # 误分类点条件：y_i * (w * x_i + b) <= 0
                condition = y_[idx] * (np.dot(x_i, self.w) + self.b) <= 0
                if condition:
                    # 更新权重和偏置
                    self.w += self.lr * y_[idx] * x_i
                    self.b += self.lr * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.w) + self.b
        return np.where(linear_output >= 0, 1, 0)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 生成二分类数据集，并且保证数据线性可分
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, 
                               n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试
    my_model = MyPerceptron(learning_rate=0.1, max_iter=1000)
    my_model.fit(X_train, y_train)
    my_preds = my_model.predict(X_test)
    print("自定义感知机准确率:", np.mean(my_preds == y_test))
    
    # sklearn实现测试
    sk_model = Perceptron(eta0=0.1, max_iter=1000, random_state=42)
    sk_model.fit(X_train, y_train)
    sk_preds = sk_model.predict(X_test)
    print("sklearn感知机准确率:", np.mean(sk_preds == y_test))
