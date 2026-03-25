import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# ==========================================
# 1. 自行实现 K-Means 聚类算法 (Self-implemented K-Means)
# ==========================================
class MyKMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None
        self.labels = None

    def fit(self, X):
        n_samples, n_features = X.shape
        
        # 1. 随机初始化聚类中心 (从数据集中随机选取 k 个点)
        np.random.seed(42)
        random_indices = np.random.choice(n_samples, self.k, replace=False)
        self.centroids = X[random_indices]
        
        for i in range(self.max_iter):
            # 2. 计算每个样本到各个聚类中心的距离，并分配到最近的簇
            # 使用 broadcasting 计算欧氏距离平方
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            
            # 3. 更新聚类中心
            new_centroids = np.zeros((self.k, n_features))
            for j in range(self.k):
                # 提取属于第 j 个簇的样本
                cluster_points = X[self.labels == j]
                if len(cluster_points) > 0:
                    new_centroids[j] = np.mean(cluster_points, axis=0)
                else:
                    # 如果簇为空，则保留原中心 (实际中通常重新随机初始化该中心)
                    new_centroids[j] = self.centroids[j]
                    
            # 4. 判断是否收敛
            center_shift = np.sum(np.linalg.norm(new_centroids - self.centroids, axis=1))
            self.centroids = new_centroids
            if center_shift < self.tol:
                break

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 生成各向同性的聚类数据
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    
    # ---------------- 自行实现测试 ----------------
    my_kmeans = MyKMeans(k=4)
    my_kmeans.fit(X)
    my_labels = my_kmeans.labels
    
    # ---------------- sklearn实现测试 ----------------
    sk_kmeans = KMeans(n_clusters=4, init='random', n_init=1, max_iter=100, random_state=42)
    sk_kmeans.fit(X)
    sk_labels = sk_kmeans.labels_
    
    print("自定义 K-Means 聚类中心:\n", my_kmeans.centroids)
    print("sklearn K-Means 聚类中心:\n", sk_kmeans.cluster_centers_)
    
    # 评估聚类效果 (轮廓系数，越接近1越好)
    print("\n自定义 K-Means 轮廓系数:", silhouette_score(X, my_labels))
    print("sklearn K-Means 轮廓系数:", silhouette_score(X, sk_labels))
