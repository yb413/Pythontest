import tensorflow as tf
import numpy

x = tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

num = tf.size(x).numpy()
a = num*tf.reduce_sum(tf.multiply(x,y))

e = tf.multiply(tf.reduce_sum(x),tf.reduce_sum(y))

c = num*tf.reduce_sum(tf.square(x))

d = tf.square(tf.reduce_sum(x))

w = tf.divide(tf.subtract(a,e),tf.subtract(c,d))

sum_y = tf.reduce_sum(y)

sum_x = num*tf.reduce_sum(x)

b = tf.divide(tf.subtract(sum_y,sum_x),num)
print("w的值为：{}\nb的值为：{}".format(w,b))