import tensorflow as tf

print('------B. Using run------')
t = tf.constant([1, 2, 3])
sess = tf.Session()
arr = sess.run(t)
print('{}\n'.format(repr(arr)))

t2 = tf.constant(4)
tup = sess.run((t, t2))
print('{}\n'.format(repr(tup)))

'''
array([1, 2, 3], dtype=int32)
(array([1, 2, 3], dtype=int32), 4)
'''

inputs = tf.placeholder(tf.float32, shape=(None, 2))
feed_dict = {
    inputs: [[1.1, -0.3],
             [0.2, 0.1]]
}
sess = tf.Session()
arr = sess.run(inputs, feed_dict=feed_dict)
print('{}\n'.format(repr(arr)))
'''
array([[ 1.1, -0.3],
       [ 0.2,  0.1]], dtype=float32)
'''
print('------C. Initializing variables------')
inputs = tf.placeholder(tf.float32, shape=(None, 2))
feed_dict = {
  inputs: [[1.1, -0.3],
           [0.2, 0.1]]
}
logits = tf.layers.dense(inputs, 1, name='logits')
init_op = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init_op) # variable initialization
arr = sess.run(logits, feed_dict=feed_dict)
print('{}\n'.format(repr(arr)))
'''
array([[-1.3331772 ],
       [-0.10937621]], dtype=float32)
'''

print('------D. Training logistics------')
# predefined dataset
print('Input data:')
print('{}\n'.format(repr(input_data)))

print('Labels:')
print('{}\n'.format(repr(input_labels)))
'''
Input data:
array([[[ 1.2,  0.3],
        [ 0.1, -0.2],
        [-0.3,  0.3]],

       [[-2.1,  1.4],
        [-0.9,  0.6],
        [ 1.2,  2.2]],

       [[-1.1,  2.3],
        [ 1.1, -0.8],
        [ 1. ,  1.1]],

       [[ 1.4, -0.8],
        [ 1.2, -2. ],
        [ 1.1,  1.8]]])

Labels:
array([[[1],
        [0],
        [1]],

       [[0],
        [1],
        [1]],

       [[1],
        [0],
        [0]],

       [[0],
        [0],
        [0]]])
'''

print('------Ex1: ------')
init_op = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init_op)


print('------Ex2: ------')
for i in range(1000):
  feed_dict = {
    inputs: input_data[i],
    labels: input_labels[i]
  }
  sess.run(train_op, feed_dict=feed_dict)

