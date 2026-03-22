import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# 1. 自行实现 AdaBoost (Self-implemented AdaBoost with Decision Stump)
# ==========================================
class DecisionStump:
    def __init__(self):
        self.polarity = 1
        self.feature_idx = None
        self.threshold = None
        self.alpha = None

    def predict(self, X):
        n_samples = X.shape[0]
        X_column = X[:, self.feature_idx]
        predictions = np.ones(n_samples)
        
        if self.polarity == 1:
            predictions[X_column < self.threshold] = -1
        else:
            predictions[X_column > self.threshold] = -1
            
        return predictions

class MyAdaBoost:
    def __init__(self, n_clf=50):
        self.n_clf = n_clf
        self.clfs = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # 将标签转为 -1 和 1
        y_ = np.where(y <= 0, -1, 1)
        
        # 初始化样本权重 w = 1/N
        w = np.full(n_samples, (1 / n_samples))
        self.clfs = []

        for _ in range(self.n_clf):
            clf = DecisionStump()
            min_error = float('inf')
            
            # 寻找当前权重下最优的决策树桩 (遍历所有特征和所有阈值)
            for feature_i in range(n_features):
                X_column = X[:, feature_i]
                thresholds = np.unique(X_column)
                
                for threshold in thresholds:
                    # 测试 polarity=1
                    p = 1
                    predictions = np.ones(n_samples)
                    predictions[X_column < threshold] = -1
                    # 错误率 = 被错分样本的权重之和
                    error = sum(w[y_ != predictions])
                    
                    if error > 0.5:
                        error = 1 - error
                        p = -1
                        
                    if error < min_error:
                        min_error = error
                        clf.polarity = p
                        clf.threshold = threshold
                        clf.feature_idx = feature_i

            # 防止 error=0 导致除零错误
            EPS = 1e-10
            # 计算分类器权重 alpha
            clf.alpha = 0.5 * np.log((1.0 - min_error + EPS) / (min_error + EPS))
            
            # 预测当前最优弱分类器的结果
            predictions = clf.predict(X)
            
            # 更新样本权重
            w *= np.exp(-clf.alpha * y_ * predictions)
            w /= np.sum(w) # 规范化
            
            self.clfs.append(clf)

    def predict(self, X):
        clf_preds = [clf.alpha * clf.predict(X) for clf in self.clfs]
        y_pred = np.sum(clf_preds, axis=0)
        # 将 -1 和 1 映射回 0 和 1 (如果需要) 或保持 -1/1
        return np.where(np.sign(y_pred) >= 0, 1, 0)

# ==========================================
# 2. 调用库实现 (Library implementation)
# ==========================================
if __name__ == "__main__":
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 自行实现测试
    my_ada = MyAdaBoost(n_clf=50)
    my_ada.fit(X_train, y_train)
    my_preds = my_ada.predict(X_test)
    print("自定义AdaBoost准确率:", accuracy_score(y_test, my_preds))
    
    # sklearn实现测试 (默认使用深度为1的决策树即DecisionStump)
    sk_ada = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, random_state=42)
    sk_ada.fit(X_train, y_train)
    sk_preds = sk_ada.predict(X_test)
    print("sklearn AdaBoost准确率:", accuracy_score(y_test, sk_preds))
