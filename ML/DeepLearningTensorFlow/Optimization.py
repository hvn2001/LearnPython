import tensorflow as tf

labels_float = tf.cast(labels, tf.float32)  # Ex1

cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(
    labels=labels_float, logits=logits)  # Ex2

loss = tf.reduce_mean(cross_entropy)  # Ex3

adam = tf.train.AdamOptimizer()  # Ex4
train_op = adam.minimize(loss)
