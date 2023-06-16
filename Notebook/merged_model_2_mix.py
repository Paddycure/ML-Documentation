# -*- coding: utf-8 -*-
"""merged_model_2_mix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FMu-EJmZUcBo8O_uy0djAdX45Y7UAmhX
"""

from google.colab import drive
drive.mount('/content/drive')

"""# Import Library"""

import os
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array, load_img

import tensorflow_hub as hub
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

from tqdm import tqdm

print("\u2022 Using TensorFlow Version:", tf.__version__)
print("\u2022 Using TensorFlow Hub Version: ", hub.__version__)
print('\u2022 GPU Device Found.' if tf.test.is_gpu_available() else '\u2022 GPU Device Not Found. Running on CPU')

"""# Load Data dari Penyimpanan G-Drive"""

train_dir = '/content/drive/MyDrive/Product-based Project - Paddycure/Machine Learning/Dataset/dataset-mix/train'
valid_dir = '/content/drive/MyDrive/Product-based Project - Paddycure/Machine Learning/Dataset/dataset-mix/valid'

train_bacterial_blight_dir = os.path.join(train_dir, 'bacterial_blight')
train_brown_spot_dir = os.path.join(train_dir, 'brown_spot')
train_healthy_dir = os.path.join(train_dir, 'healthy')
train_hispa_dir = os.path.join(train_dir, 'hispa')
train_leaf_blast_dir = os.path.join(train_dir, 'leaf_blast')
train_leaf_smut_dir = os.path.join(train_dir, 'leaf_smut')
train_tungro_dir = os.path.join(train_dir, 'tungro')

valid_bacterial_blight_dir = os.path.join(valid_dir, 'bacterial_blight')
valid_brown_spot_dir = os.path.join(valid_dir, 'brown_spot')
valid_healthy_dir = os.path.join(valid_dir, 'healthy')
valid_hispa_dir = os.path.join(valid_dir, 'hispa')
valid_leaf_blast_dir = os.path.join(valid_dir, 'leaf_blast')
valid_leaf_smut_dir = os.path.join(valid_dir, 'leaf_smut')
valid_tungro_dir = os.path.join(valid_dir, 'tungro')

import time
import os
from os.path import exists

def count(dir, counter=0):
    "returns number of files in dir and subdirs"
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return dir + " : " + str(counter) + " files"

print('total images for training :', count(train_dir))
print('total images for validation :', count(valid_dir))

print(f"Images of 'BACTERIAL BLIGHT' for training: {len(os.listdir(train_bacterial_blight_dir))}")
print(f"Images of 'BROWN SPOT' for training: {len(os.listdir(train_brown_spot_dir))}")
print(f"Images of 'HEALTHY' for training: {len(os.listdir(train_healthy_dir))}")
print(f"Images of 'HISPA' for training: {len(os.listdir(train_hispa_dir))}")
print(f"Images of 'LEAF BLAST' for training: {len(os.listdir(train_leaf_blast_dir))} ")
print(f"Images of 'LEAF SMUT' for training: {len(os.listdir(train_leaf_smut_dir))} ")
print(f"Images of 'TUNGRO' for training: {len(os.listdir(train_tungro_dir))} \n")

print(f"Images of 'BACTERIAL BLIGHT' for validation: {len(os.listdir(valid_bacterial_blight_dir))}")
print(f"Images of 'BROWN SPOT' for validation: {len(os.listdir(valid_brown_spot_dir))}")
print(f"Images of 'HEALTHY' for validation: {len(os.listdir(valid_healthy_dir))}")
print(f"Images of 'HISPA' for validation: {len(os.listdir(valid_hispa_dir))}")
print(f"Images of 'LEAF BLAST' for validation: {len(os.listdir(valid_leaf_blast_dir))} ")
print(f"Images of 'LEAF SMUT' for validation: {len(os.listdir(valid_leaf_smut_dir))} ")
print(f"Images of 'TUNGRO' for validation: {len(os.listdir(valid_tungro_dir))} \n")

"""# Melihat Data Gambar"""

bacterial_blight = [train_dir + '/bacterial_blight/' + img for img in os.listdir(train_dir + '/bacterial_blight')[:3]]
brown_spot = [train_dir + '/brown_spot/' + img for img in os.listdir(train_dir + '/brown_spot')[:3]]
healthy = [train_dir + '/healthy/' + img for img in os.listdir(train_dir + '/healthy')[:3]]
hispa = [train_dir  + '/hispa/' + img for img in os.listdir(train_dir + '/hispa')[:3]]
leaf_blast = [train_dir  + '/leaf_blast/' + img for img in os.listdir(train_dir + '/leaf_blast')[:3]]
leaf_smut = [train_dir  + '/leaf_smut/' + img for img in os.listdir(train_dir + '/leaf_smut')[:3]]
tungro = [train_dir  + '/tungro/' + img for img in os.listdir(train_dir + '/tungro')[:3]]

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(bacterial_blight):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Bacterial Blight")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(brown_spot):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Brown Spot")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(healthy):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Healthy")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(hispa):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Hispa")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(leaf_blast):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Leaf Blast")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(leaf_smut):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Leaf Smut")

from PIL import Image
plt.figure(figsize=(16,16))
for i,k  in enumerate(tungro):
    image = Image.open(k)
    plt.subplot(3,3,i+1)
    plt.imshow(image)
    plt.title("Tungro")

"""# Ekstrak Pre-Trained Model MobileNetV3"""

module_selection = ("mobilenet_v3_large_100_224", 224, 1280)
handle_base, pixels, FV_SIZE = module_selection
MODULE_HANDLE ="https://tfhub.dev/google/imagenet/{}/feature_vector/5".format(handle_base)
IMAGE_SIZE = (pixels, pixels)
print("Using {} with input size {} and output dimension {}".format(MODULE_HANDLE, IMAGE_SIZE, FV_SIZE))

do_fine_tuning = True

BATCH_SIZE = 32

feature_extractor = hub.KerasLayer(MODULE_HANDLE,
                                   input_shape=IMAGE_SIZE + (3,),
                                   output_shape=[FV_SIZE],
                                   trainable=do_fine_tuning)

"""# Image Augmentation"""

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
      rescale = 1./255,
      rotation_range=40,
      horizontal_flip=True,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      fill_mode='nearest')

training_generator = train_datagen.flow_from_directory(
    train_dir,
    shuffle=True,
    seed=42,
    color_mode="rgb",
    class_mode="categorical",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE)

validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
    valid_dir,
    shuffle=False,
    seed=42,
    color_mode="rgb",
    class_mode="categorical",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE)

class_names = os.listdir(train_dir)

print(class_names)

training_generator.class_names = class_names
validation_generator.class_names = class_names

NUM_CLASSES = len(class_names)

# AUTOTUNE = tf.data.experimental.AUTOTUNE

# def one_hot_label(image, label):
#     label = tf.one_hot(label, NUM_CLASSES)
#     return image, label

# train_ds = training_generator.map(one_hot_label, num_parallel_calls=AUTOTUNE)
# val_ds = validation_generator.map(one_hot_label, num_parallel_calls=AUTOTUNE)

# train_ds = train_ds.cache().prefetch(buffer_size = AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size = AUTOTUNE)

"""# Struktur Model"""

print("Building model with", MODULE_HANDLE)

model = tf.keras.Sequential([
        feature_extractor,
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(7, activation='softmax')
])

model.summary()

#@title (Optional) Unfreeze some layers
NUM_LAYERS = 64

if do_fine_tuning:
    feature_extractor.trainable = True

    for layer in model.layers[-NUM_LAYERS:]:
        layer.trainable = True

else:
    feature_extractor.trainable = False

if do_fine_tuning:
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.CategoricalCrossentropy(),
                  metrics=['accuracy'])
else:
    model.compile(optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

"""# Menentukan Callbacks"""

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.95 and logs.get('val_accuracy')>0.85):
      self.model.stop_training = True
      print("\nThe accuracy of the training set has reached > 90% and val_accuracy > 80%!")
callbacks = myCallback()

# EPOCHS=50

# history = model.fit(
#         train_ds,
#         epochs=EPOCHS,
#         validation_data=val_ds,
#         callbacks = [callbacks])

EPOCHS=20

history = model.fit(
        training_generator,
        epochs=EPOCHS,
        validation_data=validation_generator,
        callbacks = [callbacks])

"""# Visualisasi Hasil Training"""

# store results
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']


# plot results
# accuracy
plt.figure(figsize=(10, 16))
plt.rcParams['figure.figsize'] = [16, 9]
plt.rcParams['font.size'] = 14
plt.rcParams['axes.grid'] = True
plt.rcParams['figure.facecolor'] = 'white'
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.title(f'\nTraining and Validation Accuracy. \nTrain Accuracy:{str(acc[-1])}\nValidation Accuracy: {str(val_acc[-1])}')

# loss
plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.title(f'Training and Validation Loss. \nTrain Loss:{str(loss[-1])}\nValidation Loss: {str(val_loss[-1])}')
plt.xlabel('epoch')
plt.tight_layout(pad=3.0)
plt.show()

"""# Save Model"""

saved_model_path = '/content/drive/MyDrive/Machine Learning/model-mix'

tf.saved_model.save(model, saved_model_path)

# !tensorflowjs_converter \
#     --input_format=keras_saved_model \
#     /content/drive/MyDrive/Machine Learning/merged_model_1_95-841684242780 \
#     /tmp/linear

model.save('/content/drive/MyDrive/Machine Learning/model-mix/model-mix.h5')

!pip install tensorflowjs

import tensorflowjs as tfjs
tfjs.converters.save_keras_model(model, '/content/drive/MyDrive/Machine Learning/model-mix')