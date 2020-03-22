import numpy as np

x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

x1 = np.mean(x)
y1 = np.mean(y)

x2 = x - x1
y2 = y - y1

t = np.stack((x2,y2),axis=0)
c = np.sum(np.prod(t,axis=0))
d = np.sum(np.square(x2))

w = c / d
b = y1 - w*x1 
print("w的值为：{}\nb的值为：{}".format(w,b))