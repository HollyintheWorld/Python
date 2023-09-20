import numpy as np
import glob
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


#data preprocessing
def load_images(file_paths):
    images = []
    labels = []
    for file_path in file_paths:
        image = tf.keras.preprocessing.image.load_img(file_path, target_size=(136, 102))
        image = tf.keras.preprocessing.image.img_to_array(image) # 사진 크기가 136,102
        images.append(image)
        label = file_path.split("\\")[-2]
        labels.append(label)
    return images, labels

train_file_paths = glob.glob("./Shoes/train/**/*.jpg", recursive=True)
val_file_paths = glob.glob("./Shoes/val/**/*.jpg", recursive=True)
test_file_paths = glob.glob("./Shoes/test/**/*.jpg", recursive=True)

train_images, train_labels = load_images(train_file_paths)
val_images, val_labels = load_images(val_file_paths)
test_images, test_labels = load_images(test_file_paths)

train_images = tf.keras.applications.vgg16.preprocess_input(np.array(train_images))
val_images = tf.keras.applications.vgg16.preprocess_input(np.array(val_images))
test_images = tf.keras.applications.vgg16.preprocess_input(np.array(test_images))


#label mapping
label_map = {label: idx for idx, label in enumerate(np.unique(train_labels))}

train_labels = [label_map[label] for label in train_labels]
val_labels = [label_map[label] for label in val_labels]
test_labels = [label_map[label] for label in test_labels]

num_classes = len(np.unique(train_labels))
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes)
val_labels = tf.keras.utils.to_categorical(val_labels, num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes)


#Creating and freezing VGG16 synthetic-based layers
conv_base  = keras.applications.vgg16.VGG16(
    weights="imagenet",
    include_top=False)
conv_base.trainable = False


#Data multiplication layer
data_augmentation = keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.2),
    ]
)


#dense classifier
inputs = keras.Input(shape=(136, 102, 3))
x = data_augmentation(inputs)
x = keras.applications.vgg16.preprocess_input(x)
x = conv_base(x)
x = layers.Flatten()(x)
x = layers.Dense(128)(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(3, activation="sigmoid")(x)
model = keras.Model(inputs, outputs)
model.compile(loss="categorical_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])
callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="feature_extraction_with_data_augmentation.keras",
        save_best_only=True,
        monitor="val_loss")
]


#Model creation and val verification
history = model.fit(
    x=train_images,
    y=train_labels,
    epochs=20,
    validation_data=(val_images, val_labels),
    callbacks=callbacks)


#Testing model
temp_model = keras.Model(inputs, outputs)
temp_model.compile(loss="categorical_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])
history = temp_model.fit(
    x=train_images,
    y=train_labels,
    epochs=30,
    validation_data=(val_images, val_labels),
    callbacks=callbacks)


#Visualizing the result
import matplotlib.pyplot as plt
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, "bo", label="Training accuracy")
plt.plot(epochs, val_acc, "b", label="Validation accuracy")
plt.title("Training and validation accuracy")
plt.legend()
plt.figure()
plt.plot(epochs, loss, "bo", label="Training loss")
plt.plot(epochs, val_loss, "b", label="Validation loss")
plt.title("Training and validation loss")
plt.legend()
plt.show()


#Creating the final Model
final_model = keras.Model(inputs, outputs)
final_model.compile(loss="categorical_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])
final_model.fit(
    x=train_images,
    y=train_labels,
    epochs=20,
    callbacks=callbacks)


#testing
test_loss, test_acc = final_model.evaluate(test_images, test_labels)
print(f"test accuracy: {test_acc:.3f}")


#bringing the test image
image_path = "./신발/result/Slipper.jpg"
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(136, 102))
image_array = tf.keras.preprocessing.image.img_to_array(image)
image_array = np.expand_dims(image_array, axis=0)
preprocessed_image = tf.keras.applications.vgg16.preprocess_input(image_array)


# Making the prediction
predictions = final_model.predict(preprocessed_image)
class_index = np.argmax(predictions[0])
confidence = predictions[0][class_index]

if (class_index == 2): #2 is a slipper
    print("the input is Slippers")
else:
    print("the input is not Slippers")
