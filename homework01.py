import math

a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
c = int(input("请输入c的值："))
derta = b*b-4*a*c
if derta < 0:
    print("方程：{}x^2+{}*x+{}=0无解".format(a,b,c))
elif derta == 0:
    x = -b/2*a
    print("方程只有唯一解为：{}".format(x))
else:
    x1 = (-b+math.sqrt(derta))/2*a
    x2 = (-b-math.sqrt(derta))/2*a
    print("方程：{}x^2+{}*x+{}=0 的解分别为：x1={}，x2={}".format(a,b,c,x1,x2))