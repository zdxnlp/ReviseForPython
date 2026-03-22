import numpy as np
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. 自行实现 K 近邻算法 (Self-implemented KNN)
# ==========================================
class MyKNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        # KNN 是懒惰学习算法，fit 过程只保存数据
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X):
        predictions = [self._predict_single(x) for x in X]
        return np.array(predictions)

    def _predict_single(self, x):
        # 1. 计算当前样本与所有训练样本的欧氏距离
        distances = [np.sqrt(np.sum((x - x_train) ** 2)) for x_train in self.X_train]
        
        # 2. 按照距离排序，获取前 k 个最近邻样本的索引
        k_indices = np.argsort(distances)[:self.k]
        
        # 3. 获取前 k 个样本的标签
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # 4. 多数表决，返回出现次数最多的标签
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 加载鸢尾花数据集
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试
    my_knn = MyKNN(k=3)
    my_knn.fit(X_train, y_train)
    my_preds = my_knn.predict(X_test)
    print("自定义KNN准确率:", accuracy_score(y_test, my_preds))
    
    # sklearn实现测试
    sk_knn = KNeighborsClassifier(n_neighbors=3)
    sk_knn.fit(X_train, y_train)
    sk_preds = sk_knn.predict(X_test)
    print("sklearn KNN准确率:", accuracy_score(y_test, sk_preds))
