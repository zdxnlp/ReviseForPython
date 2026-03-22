import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# ==========================================
# 1. 自行实现 EM 算法求解高斯混合模型 (GMM)
# ==========================================
class MyGMM:
    def __init__(self, n_components=2, max_iter=100, tol=1e-4):
        self.K = n_components
        self.max_iter = max_iter
        self.tol = tol
        # 参数
        self.weights = None
        self.means = None
        self.covariances = None

    def _multivariate_gaussian(self, X, mean, cov):
        n = X.shape[1]
        diff = X - mean
        # 计算高斯概率密度
        factor = 1.0 / (np.sqrt((2 * np.pi) ** n * np.linalg.det(cov)))
        exponent = -0.5 * np.sum(np.dot(diff, np.linalg.inv(cov)) * diff, axis=1)
        return factor * np.exp(exponent)

    def fit(self, X):
        n_samples, n_features = X.shape
        
        # 1. 初始化参数 (随机选择K个点作为均值，权重均分，协方差为单位矩阵)
        np.random.seed(42)
        random_idx = np.random.choice(n_samples, self.K, replace=False)
        self.means = X[random_idx]
        self.weights = np.ones(self.K) / self.K
        self.covariances = np.array([np.eye(n_features) for _ in range(self.K)])
        
        log_likelihood = 0
        
        for i in range(self.max_iter):
            # ================= E 步 =================
            # 计算响应度 (即隐变量的后验概率 gamma)
            gamma = np.zeros((n_samples, self.K))
            for k in range(self.K):
                gamma[:, k] = self.weights[k] * self._multivariate_gaussian(X, self.means[k], self.covariances[k])
            
            # 计算对数似然 (用于判断收敛)
            new_log_likelihood = np.sum(np.log(np.sum(gamma, axis=1)))
            
            # 归一化响应度
            gamma = gamma / np.sum(gamma, axis=1, keepdims=True)
            
            # ================= M 步 =================
            N_k = np.sum(gamma, axis=0) # 每个聚类的有效样本数
            
            for k in range(self.K):
                # 更新权重
                self.weights[k] = N_k[k] / n_samples
                # 更新均值
                self.means[k] = np.sum(gamma[:, k:k+1] * X, axis=0) / N_k[k]
                # 更新协方差
                diff = X - self.means[k]
                self.covariances[k] = np.dot((gamma[:, k:k+1] * diff).T, diff) / N_k[k]
                # 加上微小值防止奇异矩阵
                self.covariances[k] += np.eye(n_features) * 1e-6
                
            # 检查收敛
            if np.abs(new_log_likelihood - log_likelihood) < self.tol:
                break
            log_likelihood = new_log_likelihood

    def predict(self, X):
        gamma = np.zeros((X.shape[0], self.K))
        for k in range(self.K):
            gamma[:, k] = self.weights[k] * self._multivariate_gaussian(X, self.means[k], self.covariances[k])
        return np.argmax(gamma, axis=1)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 生成二维聚类数据
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)
    
    # 自行实现测试
    my_gmm = MyGMM(n_components=3, max_iter=100)
    my_gmm.fit(X)
    my_preds = my_gmm.predict(X)
    print("自定义GMM聚类完成，均值:\n", my_gmm.means)
    
    # sklearn实现测试
    sk_gmm = GaussianMixture(n_components=3, max_iter=100, random_state=42)
    sk_gmm.fit(X)
    sk_preds = sk_gmm.predict(X)
    print("sklearn GMM聚类完成，均值:\n", sk_gmm.means_)
