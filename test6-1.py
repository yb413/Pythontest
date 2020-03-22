import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

housing = np.array([[137.97,145.00],[104.50,110.00],[100.00,93.00],[124.32,116.00],[79.20,65.32],[99.00,104.00],[124.00,118.00],[114.00,91.00],[106.69,62.00],[138.05,133.00],[53.75,51.00],[46.91,45.00],[68.00,78.50],[63.02,69.65],[81.26,75.69],[86.21,95.30]])

plt.scatter(housing[:,0],housing[:,1],marker='o',color='red')
plt.xlabel('面积（平方米）',fontsize=14)
plt.ylabel("价格（万元）",fontsize=14)
plt.title("商品房纪录",color='b',fontsize=16)
plt.show()
