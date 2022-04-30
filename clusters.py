import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
     
x1 = np.array([1, 2, 3, 2, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Sample')
plt.scatter(x1, x2)
plt.show()

clusters=3
 
kmeans_model = KMeans(n_clusters=clusters).fit(X)
print ('Результаты кластеризации:', kmeans_model.labels_) # Результаты кластеризации: [1 1 1 1 1 0 0 0 0 0 2 2 2 2 2]
colors = ['black', 'green', 'red']  
markers = ['o', 's', 'D']  
 
for i, l in enumerate(kmeans_model.labels_):  
    plt.plot(x1[i], x2[i], color=colors[l],marker=markers[l],ls='None')  
    plt.xlim([0, 10])  
    plt.ylim([0, 10])  
    plt.title('K = %s' %(clusters)) 
plt.show()