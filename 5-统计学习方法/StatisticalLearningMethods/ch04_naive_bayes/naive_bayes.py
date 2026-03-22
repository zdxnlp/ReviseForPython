import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. 自行实现朴素贝叶斯 (Self-implemented Naive Bayes)
# ==========================================
class MyGaussianNB:
    def fit(self, X, y):
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        n_features = X.shape[1]
        
        # 存储每个类别的均值、方差和先验概率
        self.mean = np.zeros((n_classes, n_features))
        self.var = np.zeros((n_classes, n_features))
        self.priors = np.zeros(n_classes)
        
        for idx, c in enumerate(self.classes):
            X_c = X[y == c]
            self.mean[idx, :] = X_c.mean(axis=0)
            self.var[idx, :] = X_c.var(axis=0)
            self.priors[idx] = X_c.shape[0] / float(X.shape[0])
            
    def _pdf(self, class_idx, x):
        # 高斯概率密度函数
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp(- (x - mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    def _predict_single(self, x):
        posteriors = []
        
        for idx, c in enumerate(self.classes):
            # 先验概率的对数
            prior = np.log(self.priors[idx])
            # 条件概率的对数和 (假设特征独立)
            posterior = np.sum(np.log(self._pdf(idx, x)))
            posteriors.append(prior + posterior)
            
        return self.classes[np.argmax(posteriors)]

    def predict(self, X):
        return np.array([self._predict_single(x) for x in X])

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 加载乳腺癌数据集 (连续特征，适合高斯朴素贝叶斯)
    data = load_breast_cancer()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试
    my_nb = MyGaussianNB()
    my_nb.fit(X_train, y_train)
    my_preds = my_nb.predict(X_test)
    print("自定义高斯朴素贝叶斯准确率:", accuracy_score(y_test, my_preds))
    
    # sklearn实现测试
    sk_nb = GaussianNB()
    sk_nb.fit(X_train, y_train)
    sk_preds = sk_nb.predict(X_test)
    print("sklearn高斯朴素贝叶斯准确率:", accuracy_score(y_test, sk_preds))
