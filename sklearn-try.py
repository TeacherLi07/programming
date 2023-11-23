import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

data=load_iris()

X = np.array([[1, 2], [2, 3], [2, 5], [3, 2], [3, 3], [4, 5]])

k=2
k = 2  # 指定要分为的簇的数量
model = KMeans(n_clusters=k)

# 拟合模型
model.fit(X)

# 获取簇中心点
cluster_centers = model.cluster_centers_

# 预测每个样本所属的簇
labels = model.labels_

print("簇中心点:", cluster_centers)
print("样本所属簇:", labels)
