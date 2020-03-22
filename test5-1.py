import numpy as np

np.random.seed(612)
a = np.random.rand(1000)
b = int(input("请输入一个1-100的整数："))

print("序号\t索引值\t随机数")
d = 0
for i in range(1,1000):
    if i % b == 0:
        d += 1
        print("{}\t{}\t{}\t".format(d,i,a[i]))