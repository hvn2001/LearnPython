import tensorflow as tf

probs = tf.nn.sigmoid(logits)  # Ex1

rounded_probs = tf.round(probs)  # Ex2

predictions = tf.cast(rounded_probs, tf.int32)  # Ex3

is_correct = tf.equal(predictions, labels)  # Ex4

is_correct_float = tf.cast(is_correct, tf.float32)  # Ex5
accuracy = tf.reduce_mean(is_correct_float)
