import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_,_) = boston_housing.load_data(test_split=0)

titles = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B-1000','LSTAT','MEDV']
print("1--CRIM\n2--ZN\n3--IDUS\n4--CHAS\n5--NOX\n6--RM\n7--AGE\n8--DIS\n9--RAD\n10--TAX\n11--PTRATIO\n12--B\n13--LSTAT")
a = int(input("请选择对应属性的编号："))
plt.figure(figsize=(12,12))

for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i)+"."+titles[i]+'- Price')
plt.tight_layout()
plt.figure(num=3,figsize=(8,8))
plt.scatter(train_x[:,a-1],train_y)
plt.xlabel(titles[a-1])
plt.ylabel("Price($1000's)")
plt.suptitle("1--CRIM\n2--ZN\n3--IDUS\n4--CHAS\n5--NOX\n6--RM\n7--AGE\n8--DIS\n9--RAD\n10--TAX\n11--PTRATIO\n12--B\n13--LSTAT")
plt.title(str(a)+"."+titles[a-1]+"- Price")
plt.tight_layout(rect=[0,0,1,0.6])
plt.show()