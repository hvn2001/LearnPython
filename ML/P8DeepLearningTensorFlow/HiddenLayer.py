import tensorflow as tf


def model_layers(inputs, output_size):
    hidden1 = tf.layers.dense(inputs, 5,
                              activation=tf.nn.relu,
                              name='hidden1')
    logits = tf.layers.dense(hidden1, output_size,
                             name='logits')
    return logits
