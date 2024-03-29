import tensorflow as tf
import datetime as dt


def hello_world():
    print("This is the world we live in...")


def tf_test(device):
    with tf.device(f"/{device}:0"):
        # print(f"Tensorflow version: {tf.__version__}")
        # print(f"Tensorflow.keras version: {tf.keras.__version__}")

        # print(tf.test.is_built_with_cuda())
        # print(tf.config.list_physical_devices('GPU'))
        # print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

        # get the MNIST data set
        mnist = tf.keras.datasets.mnist
        # load data and divide
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

        # model
        model = tf.keras.models.Sequential()
        model.add(
            tf.keras.layers.Conv2D(
                32, (5, 5), activation="relu", input_shape=(28, 28, 1)
            )
        )
        # add new layers
        model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        model.add(tf.keras.layers.Conv2D(64, (5, 5), activation="relu"))
        model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        # model.summary()

        # classifier layer
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(10, activation="softmax"))
        # model.summary()

        # print("Training images:\n{}".format(train_images.shape))
        # print("Training labels:\n{}".format(train_labels.shape))

        # reshape the data
        train_images = train_images.reshape((60000, 28, 28, 1))
        train_images = train_images.astype("float32") / 255

        test_images = test_images.reshape((10000, 28, 28, 1))
        test_images = test_images.astype("float32") / 255

        train_labels = tf.keras.utils.to_categorical(train_labels)
        test_labels = tf.keras.utils.to_categorical(test_labels)

        # print("\nAfter reshaping...")
        # print("Training images:\n{}".format(train_images.shape))
        # print("Training labels:\n{}".format(train_labels.shape))

        # compile the model
        model.compile(
            loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]
        )

        # check time taken on the GPU for training and testing

        start = dt.datetime.now()

        # train the model on training data
        model.fit(train_images, train_labels, batch_size=200, epochs=1, verbose=1)

        # validate the model on test data
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        end = dt.datetime.now()

        print("Test accuracy: {}".format(test_acc))
        print(f"\nTime taken on the {device}: {end - start}")
