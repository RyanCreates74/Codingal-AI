import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train/255.0, x_test/255.0
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

augment = tf.keras.Sequential([layers.RandomRotation(0.1)])

model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    augment,
    layers.Flatten(),
    layers.Dense(128, activation='leaky_relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.RMSprop(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=7)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

predictions = model.predict(x_test)

plt.imshow(x_test[0].squeeze(), cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}, True: {y_test[0]}")
plt.show()