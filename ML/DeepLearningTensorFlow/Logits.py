import tensorflow as tf


def model_layers(inputs, output_size):
    logits = tf.layers.dense(inputs, output_size,
                             name='logits')
    return logits
