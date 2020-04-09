feed_dict = {inputs: test_data, labels: test_labels}
eval_acc = sess.run(accuracy, feed_dict=feed_dict)
