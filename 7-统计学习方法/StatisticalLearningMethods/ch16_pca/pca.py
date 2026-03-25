import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as SklearnPCA
from sklearn.datasets import load_iris

# ==========================================
# 1. 自行实现主成分分析 (Self-implemented PCA using Eigenvalue Decomposition)
# ==========================================
class MyPCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None
        self.explained_variance_ratio_ = None

    def fit(self, X):
        # 1. 数据中心化 (去均值)
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # 2. 计算协方差矩阵 (注意除以 N-1，对应 ddof=1，虽然 numpy 默认除以 N，但 PCA 结果方向不变)
        # np.cov 默认期望每行代表一个变量，所以传入转置
        cov_matrix = np.cov(X_centered.T)
        
        # 3. 计算协方差矩阵的特征值和特征向量
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # 4. 按照特征值降序排序
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # 5. 提取前 n_components 个特征向量作为主成分
        self.components = eigenvectors[:, :self.n_components]
        
        # 计算解释方差比
        total_variance = np.sum(eigenvalues)
        self.explained_variance_ratio_ = eigenvalues[:self.n_components] / total_variance

    def transform(self, X):
        # 将数据投影到主成分空间
        X_centered = X - self.mean
        return np.dot(X_centered, self.components)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 使用鸢尾花数据集 (4维特征)
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # ---------------- 1. 自行实现 PCA ----------------
    my_pca = MyPCA(n_components=2)
    my_pca.fit(X)
    X_my_reduced = my_pca.transform(X)
    
    print("自定义 PCA 主成分 (特征向量):\n", my_pca.components)
    print("自定义 PCA 解释方差比:", my_pca.explained_variance_ratio_)
    
    # ---------------- 2. sklearn PCA ----------------
    sk_pca = SklearnPCA(n_components=2)
    X_sk_reduced = sk_pca.fit_transform(X)
    
    print("\nsklearn PCA 主成分 (特征向量):\n", sk_pca.components_.T) # sklearn 的 components_ 是按行排列的，所以转置比较
    print("sklearn PCA 解释方差比:", sk_pca.explained_variance_ratio_)
    
    # 注：由于特征向量的方向可能有正负之差，所以输出的值可能会互为相反数，这是正常的，不影响投影所在的一维直线/二维平面。
    
    # ---------------- 3. 可视化降维结果 ----------------
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    scatter1 = plt.scatter(X_my_reduced[:, 0], X_my_reduced[:, 1], c=y, cmap='viridis', edgecolor='k')
    plt.title('Self-implemented PCA (2D)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    
    plt.subplot(1, 2, 2)
    scatter2 = plt.scatter(X_sk_reduced[:, 0], X_sk_reduced[:, 1], c=y, cmap='viridis', edgecolor='k')
    plt.title('Sklearn PCA (2D)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    
    plt.tight_layout()
    plt.savefig('pca_comparison.png')
    print("\n已生成对比图：pca_comparison.png")
