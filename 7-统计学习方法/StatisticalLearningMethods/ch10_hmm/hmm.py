import numpy as np
# 提示: hmmlearn 需要额外安装 (pip install hmmlearn)
try:
    from hmmlearn import hmm
    HAS_HMMLEARN = True
except ImportError:
    HAS_HMMLEARN = False

# ==========================================
# 1. 自行实现 HMM 维特比算法 (Self-implemented Viterbi Algorithm for Decoding)
# ==========================================
class MyHMM:
    def __init__(self, pi, A, B):
        """
        pi: 初始状态概率向量 (N,)
        A: 状态转移概率矩阵 (N, N)
        B: 观测概率矩阵 (N, M)
        """
        self.pi = np.array(pi)
        self.A = np.array(A)
        self.B = np.array(B)
        self.N = self.A.shape[0]

    def viterbi(self, obs_seq):
        T = len(obs_seq)
        
        # 初始化 delta (记录最大概率) 和 psi (记录路径)
        delta = np.zeros((T, self.N))
        psi = np.zeros((T, self.N), dtype=int)
        
        # t = 0
        delta[0] = self.pi * self.B[:, obs_seq[0]]
        
        # 递推 t = 1, 2, ..., T-1
        for t in range(1, T):
            for i in range(self.N):
                # 计算从上一时刻的所有状态 j 转移到当前状态 i 的概率
                prob_trans = delta[t-1] * self.A[:, i]
                # 记录最大概率并乘以观测概率
                delta[t, i] = np.max(prob_trans) * self.B[i, obs_seq[t]]
                # 记录最大概率对应的上一时刻状态 j
                psi[t, i] = np.argmax(prob_trans)
                
        # 终止
        P_best = np.max(delta[T-1])
        q_best = np.zeros(T, dtype=int)
        q_best[T-1] = np.argmax(delta[T-1])
        
        # 路径回溯
        for t in range(T-2, -1, -1):
            q_best[t] = psi[t+1, q_best[t+1]]
            
        return q_best, P_best

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    # 假设状态集合 Q = {1, 2, 3} (对应索引 0, 1, 2)
    # 观测集合 V = {红, 白} (对应索引 0, 1)
    
    pi = [0.2, 0.4, 0.4]
    A = [[0.5, 0.2, 0.3],
         [0.3, 0.5, 0.2],
         [0.2, 0.3, 0.5]]
    B = [[0.5, 0.5],
         [0.4, 0.6],
         [0.7, 0.3]]
    
    # 观测序列 O = (红, 白, 红) -> 索引 [0, 1, 0]
    obs_seq = [0, 1, 0]
    
    # 1. 自行实现维特比算法测试
    my_hmm = MyHMM(pi, A, B)
    best_path, best_prob = my_hmm.viterbi(obs_seq)
    print("自定义HMM维特比解码最优路径:", best_path)
    print("对应概率:", best_prob)
    
    # 2. sklearn (hmmlearn) 实现测试
    if HAS_HMMLEARN:
        model = hmm.CategoricalHMM(n_components=3, random_state=42)
        model.startprob_ = np.array(pi)
        model.transmat_ = np.array(A)
        model.emissionprob_ = np.array(B)
        
        # hmmlearn 要求的输入格式为二维数组 (T, 1)
        obs_seq_arr = np.array([obs_seq]).T
        logprob, sk_path = model.decode(obs_seq_arr, algorithm="viterbi")
        print("hmmlearn 维特比解码最优路径:", sk_path)
        print("对应对数概率:", logprob)
    else:
        print("提示: 未安装 hmmlearn，跳过库调用测试。可通过 'pip install hmmlearn' 安装。")
