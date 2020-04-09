import tensorflow as tf

# 10 Numeric Columns
def add_numeric_columns(feature_columns):
    numeric_features = ['Size', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    for feature_name in numeric_features:
        feature_col = tf.feature_column.numeric_column(feature_name, shape=())
    feature_columns.append(feature_col)


# 11 Indicator Columns
def add_indicator_columns(final_dataset, feature_columns):
    indicator_features = ['IsHoliday', 'Type']
    for feature_name in indicator_features:
        dtype = tf.string if feature_name == 'Type' else tf.int64
        vocab_list = list(final_dataset[feature_name].unique())
        vocab_col = tf.feature_column.categorical_column_with_vocabulary_list(
            feature_name, vocab_list, dtype=dtype)
        feature_col = tf.feature_column.indicator_column(vocab_col)
        feature_columns.append(feature_col)


# 12 Embedding Columns
def add_embedding_columns(final_dataset, feature_columns):
    embedding_features = ['Store', 'Dept']
    for feature_name in embedding_features:
        vocab_list = list(final_dataset[feature_name].unique())
        vocab_feature_col = tf.feature_column.categorical_column_with_vocabulary_list(
            feature_name, vocab_list, dtype=tf.int64)
        embedding_dim = int(len(vocab_list) ** 0.25)
        feature_col = tf.feature_column.embedding_column(vocab_feature_col, embedding_dim)
        feature_columns.append(feature_col)


# 13 Model Input Layer
def create_feature_columns(final_dataset):
    feature_columns = []
    add_numeric_columns(feature_columns)
    add_indicator_columns(final_dataset, feature_columns)
    add_embedding_columns(final_dataset, feature_columns)
    return feature_columns


def create_tensorflow_dataset(param, batch_size):
    # ?
    pass

# -----------------------------------------------------------

class SalesModel(object):
    def __init__(self, hidden_layers):
        self.hidden_layers = hidden_layers

    def run_regression_predict(self, ckpt_dir, data_file):
        regression_model = self.create_regression_model(ckpt_dir)
        input_fn = lambda: create_tensorflow_dataset(data_file, 1, training=False, has_labels=False)
        predictions = regression_model.predict(input_fn)
        pred_list = []
        for pred_dict in predictions:
            pred_list.append(pred_dict['predictions'][0])
        return pred_list

    def run_regression_eval(self, ckpt_dir):
        regression_model = self.create_regression_model(ckpt_dir)
        input_fn = lambda: create_tensorflow_dataset('eval.tfrecords', 50, training=False)
        return regression_model.evaluate(input_fn)

    def run_regression_training(self, ckpt_dir, batch_size, num_training_steps=None):
        regression_model = self.create_regression_model(ckpt_dir)
        input_fn = lambda: create_tensorflow_dataset('train.tfrecords', batch_size)
        regression_model.train(input_fn, steps=num_training_steps)

    def create_regression_model(self, ckpt_dir):
        config = tf.estimator.RunConfig(log_step_count_steps=5000)
        regression_model = tf.estimator.Estimator(
            self.regression_fn,
            config=config,
            model_dir=ckpt_dir)
        return regression_model

    def regression_fn(self, features, labels, mode, params):
        feature_columns = create_feature_columns()
        inputs = tf.feature_column.input_layer(features, feature_columns)
        batch_predictions = self.model_layers(inputs)
        predictions = tf.squeeze(batch_predictions)
        if labels is not None:
            loss = tf.losses.absolute_difference(labels, predictions)

        if mode == tf.estimator.ModeKeys.TRAIN:
            global_step = tf.train.get_or_create_global_step()
            adam = tf.train.AdamOptimizer()
            train_op = adam.minimize(
                loss, global_step=global_step)
            return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)
        if mode == tf.estimator.ModeKeys.EVAL:
            return tf.estimator.EstimatorSpec(mode, loss=loss)
        if mode == tf.estimator.ModeKeys.PREDICT:
            prediction_info = {
                'predictions': batch_predictions
            }
            return tf.estimator.EstimatorSpec(mode, predictions=prediction_info)

    def model_layers(self, inputs):
        layer = inputs
        for num_nodes in self.hidden_layers:
            layer = tf.layers.dense(layer, num_nodes,
                                    activation=tf.nn.relu)
        batch_predictions = tf.layers.dense(layer, 1)
        return batch_predictions
