import numpy as np
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt

# ==========================================
# 1. 自行实现奇异值分解 (Self-implemented SVD using Eigenvalue Decomposition)
# 注：实际工业界（如 scipy.linalg.svd）通常使用更稳定的迭代算法（如 Golub-Reinsch 算法或分治法），
# 这里为了教学目的，展示基于矩阵乘积的特征值分解方法。
# ==========================================
def my_svd(A):
    """
    计算矩阵 A 的奇异值分解: A = U * Sigma * V^T
    """
    # 1. 计算 A^T * A
    ATA = np.dot(A.T, A)
    # 计算 A^T * A 的特征值和特征向量 (对应 V)
    eigenvalues_v, V = np.linalg.eigh(ATA)
    
    # 将特征值降序排列
    idx_v = np.argsort(eigenvalues_v)[::-1]
    eigenvalues_v = eigenvalues_v[idx_v]
    V = V[:, idx_v]
    
    # 奇异值是特征值的平方根 (过滤掉负数特征值造成的微小复数)
    singular_values = np.sqrt(np.maximum(eigenvalues_v, 0))
    
    # 2. 计算 A * A^T
    AAT = np.dot(A, A.T)
    # 计算 A * A^T 的特征值和特征向量 (对应 U)
    eigenvalues_u, U = np.linalg.eigh(AAT)
    
    # 将特征值降序排列
    idx_u = np.argsort(eigenvalues_u)[::-1]
    U = U[:, idx_u]
    
    # 3. 构造对角矩阵 Sigma
    Sigma = np.zeros(A.shape)
    for i in range(min(A.shape[0], A.shape[1])):
        Sigma[i, i] = singular_values[i]
        
    # 注：直接分别求 U 和 V 可能会出现符号不一致的问题。
    # 严谨的做法是：U_i = (1/sigma_i) * A * V_i
    # 这里为了修正符号，重新根据 A 和 V 构造非零奇异值对应的 U
    for i in range(min(A.shape[0], A.shape[1])):
        if singular_values[i] > 1e-10:
            U[:, i] = np.dot(A, V[:, i]) / singular_values[i]
            
    # 返回 U, 一维奇异值数组, V的转置
    return U, singular_values, V.T

# ==========================================
# 2. 截断奇异值分解 (用于降维/近似)
# ==========================================
def my_truncated_svd(A, k):
    U, s, VT = np.linalg.svd(A, full_matrices=False) # 这里借用 numpy 稳定的 svd
    # 截取前 k 个奇异值
    U_k = U[:, :k]
    s_k = s[:k]
    VT_k = VT[:k, :]
    
    # 重构矩阵 A_approx
    A_approx = np.dot(U_k, np.dot(np.diag(s_k), VT_k))
    return A_approx

# ==========================================
# 3. 调用库实现与测试
# ==========================================
if __name__ == "__main__":
    # 创建一个简单的用户-物品评分矩阵 (例如推荐系统中的矩阵)
    # 5个用户，4个物品
    A = np.array([
        [5, 5, 0, 0],
        [5, 4, 0, 0],
        [4, 5, 0, 0],
        [0, 0, 4, 5],
        [0, 0, 5, 5]
    ], dtype=float)
    
    print("原始矩阵 A:")
    print(A)
    print("-" * 40)
    
    # ---------------- 1. numpy SVD ----------------
    U_np, s_np, VT_np = np.linalg.svd(A)
    print("NumPy SVD 奇异值:", s_np)
    
    # ---------------- 2. 自定义 SVD ----------------
    U_my, s_my, VT_my = my_svd(A)
    print("自定义 SVD 奇异值:", s_my[:min(A.shape)])
    
    # 验证自定义 SVD 的重构误差
    Sigma_my = np.zeros(A.shape)
    for i in range(min(A.shape)):
        Sigma_my[i, i] = s_my[i]
    A_reconstruct = np.dot(U_my, np.dot(Sigma_my, VT_my))
    print("\n自定义 SVD 重构矩阵:")
    print(np.round(A_reconstruct, 2))
    
    print("-" * 40)
    # ---------------- 3. sklearn TruncatedSVD (截断SVD) ----------------
    # 降维到 k=2 (提取主要特征)
    svd_sklearn = TruncatedSVD(n_components=2, random_state=42)
    A_reduced = svd_sklearn.fit_transform(A)
    print("sklearn 降维后的矩阵 (n_components=2):")
    print(np.round(A_reduced, 2))
