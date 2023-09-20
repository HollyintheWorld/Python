import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)

#preprocessing the data
def vectorize_sequences(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            results[i,j] = 1
    return results
x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train=np.asarray(train_labels).astype("float32")
y_test=np.asarray(test_labels).astype("float32")


#Creating a Model
model = keras.Sequential ([
    layers.Dense(16,activation="relu"),
    layers.Dense(16,activation="relu"),
    layers.Dense(1,activation="sigmoid"),
])

model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["accuracy"])

#Parting to train and validation data
x_val = x_train[:10000]
partial_x_train=x_train[10000:]
y_val = y_train[:10000]
partial_y_train=y_train[10000:]


#Training
history= model.fit(partial_x_train,
                  partial_y_train,
                  epochs=4,
                  batch_size=512,
                  validation_data=(x_val,y_val))

#Visualizing the loss
history_dict=history.history
loss_values=history_dict["loss"]
val_loss_values=history_dict["val_loss"]
epochs=range(1,len(loss_values)+1)
plt.plot(epochs,loss_values,"bo", label="Training loss")
plt.plot(epochs, val_loss_values,"b", label="validation loss")
plt.title("training and validation loss")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.legend()
plt.show()

#Visualizing the accuracy
plt.clf()
acc= history_dict["accuracy"]
val_acc=history_dict["val_accuracy"]
plt.plot(epochs,acc,"bo",label="Training acc")
plt.plot(epochs,val_acc,"b",label="Validation acc")
plt.title("Training and validation accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


model.predict(x_test)

#Applied model
model = keras.Sequential([
    layers.Dense(16,activation="tanh"),
    layers.Dense(16,activation="tanh"),
    layers.Dense(1,activation="sigmoid"),
])
model.compile(optimizer="rmsprop",
             loss="binary_crossentropy",
             metrics=["accuracy"])
model.fit(x_train, y_train, epochs=4, batch_size=512)
results=model.evaluate(x_test, y_test)
results
