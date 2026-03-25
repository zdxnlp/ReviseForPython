import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. 自行实现线性 SVM (Self-implemented Linear SVM using Gradient Descent on Hinge Loss)
# 注：此处为了简化，未实现复杂的SMO算法，而是使用次梯度下降法求解软间隔线性SVM
# ==========================================
class MyLinearSVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param # 正则化参数，对应 1/C
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # 将标签转换为 -1 和 1
        y_ = np.where(y <= 0, -1, 1)
        
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                # 检查是否满足函数间隔 >= 1 (Hinge Loss)
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    # 分类正确且在间隔边界外，梯度仅来自正则化项
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    # 分类错误或在间隔边界内，梯度来自损失项和正则化项
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx] # 注意：此处 b 的符号约定为 w*x - b

    def predict(self, X):
        approx = np.dot(X, self.w) - self.b
        return np.where(np.sign(approx) >= 0, 1, 0)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    X, y = make_blobs(n_samples=200, centers=2, random_state=42, cluster_std=1.2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试 (次梯度下降求解)
    my_svm = MyLinearSVM(learning_rate=0.01, lambda_param=0.01, n_iters=1000)
    my_svm.fit(X_train, y_train)
    my_preds = my_svm.predict(X_test)
    print("自定义线性SVM准确率:", accuracy_score(y_test, my_preds))
    
    # sklearn实现测试 (支持核函数，默认 RBF)
    sk_svm = SVC(kernel='linear', C=1.0)
    sk_svm.fit(X_train, y_train)
    sk_preds = sk_svm.predict(X_test)
    print("sklearn线性SVM准确率:", accuracy_score(y_test, sk_preds))
    
    sk_svm_rbf = SVC(kernel='rbf', C=1.0)
    sk_svm_rbf.fit(X_train, y_train)
    sk_rbf_preds = sk_svm_rbf.predict(X_test)
    print("sklearn RBF核SVM准确率:", accuracy_score(y_test, sk_rbf_preds))
