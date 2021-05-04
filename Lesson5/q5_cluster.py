import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
# center_num指明聚类中心个数
center_num = 7
# iter_num指明聚类迭代次数
iter_num = 10
data_frame = pd.read_excel(r"./L6data.xlsx")
class_id = [i for i in range(center_num)]
idx = [0] * len(data_frame)
distances = [0] * len(data_frame)
colors = ['red', 'green', 'blue', 'black', 'pink', 'cyan', 'yellow', 'orange', 'purple']
def initCenters(distances, center_num):
    max_distance = max(distances)
    min_distance = min(distances)
    centers = []
    for _ in range(center_num):
        centers.append(random.uniform(min_distance, max_distance))
    return centers

def get_class_id(distance, centers):
    centers = np.array(centers)
    centers = np.abs(centers - distance)
    centers = list(centers)
    return centers.index(min(centers))

def getNew(centers, distances):
    newCenters = [0] * len(centers)
    length = [0] * len(centers)
    for j in range(len(distances)):
        newCenters[idx[j]] += distances[j]
        length[idx[j]] += 1
    
    for i in range(len(centers)):
        if length[i] == 0:
            newCenters[i] = 0
        else:
            newCenters[i] /= length[i]
    return newCenters
    
def clusterIter(centers,  distances, iter_times):
    for _ in range(iter_times):
        print(centers)
        for j in range(len(distances)):
            idx[j] = get_class_id(distances[j], centers)
        centers = getNew(centers, distances)  
    X = [[] for _ in range(center_num)]
    Y = [[] for _ in range(center_num)]
    for i in range(len(idx)):
        X[idx[i]].append(data_frame.iloc[i].values[0])
        Y[idx[i]].append(data_frame.iloc[i].values[1])
        
    _, ax = plt.subplots(1, 1)
    for i in range(center_num):
        ax.scatter(X[i], Y[i], color=colors[i])
    plt.title("centerNum: " + str(center_num))
    plt.show()    
    return      
    
for i in range(len(data_frame)):
    distances[i] = np.sqrt(data_frame.iloc[i].values[0] ** 2 + data_frame.iloc[i].values[1] ** 2)
# 获取第一次的质心
centers = initCenters(distances, center_num)
clusterIter(centers, distances, iter_num)

   
