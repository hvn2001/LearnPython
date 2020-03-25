import tensorflow as tf

print('------A. The softmax function------')
t = tf.constant([[0.4, -0.8, 1.3],
                 [0.2, -1.2, -0.4]])
softmax_t = tf.nn.softmax(t)
sess = tf.Session()
print('{}\n'.format(repr(sess.run(t))))
print('{}\n'.format(repr(sess.run(softmax_t))))
'''
array([[ 0.4, -0.8,  1.3],
       [ 0.2, -1.2, -0.4]], dtype=float32)

array([[0.2659011 , 0.08008787, 0.65401113],
       [0.5569763 , 0.13734867, 0.30567506]], dtype=float32)
'''

print('------B. Predictions------')
probs = tf.constant([[0.4, 0.3, 0.3],
                     [0.2, 0.7, 0.1]])
preds = tf.argmax(probs, axis=-1)
sess = tf.Session()
print('{}\n'.format(repr(sess.run(probs))))
print('{}\n'.format(repr(sess.run(preds))))

'''
array([[0.4, 0.3, 0.3],
       [0.2, 0.7, 0.1]], dtype=float32)

array([0, 1])

'''

print('------Ex1: ------')

probs = tf.nn.softmax(logits)
predictions = tf.argmax(probs, axis=-1)

print('------Ex2: ------')

class_labels = tf.argmax(labels, axis=-1)
is_correct = tf.equal(predictions, class_labels)

print('------Ex3: ------')
cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
    labels=labels, logits=logits)
