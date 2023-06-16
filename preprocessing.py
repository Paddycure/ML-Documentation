import numpy as np
# import tensorflow_hub as hub
# from tensorflow.python.keras.preprocessing import image
# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
from PIL import Image
# from keras.utils import img_to_array

# model = load_model(('models/model.h5'),
#                    compile=False,
#                    custom_objects={'KerasLayer':hub.KerasLayer})

def preprocessing_image(img_path):
    # image = image.load_img(img_path, target_size=(224, 224, 3))
    # image = image.img_to_array(image)
    # image = np.expand_dims(image, axis=0)
    
    # op_img = Image.open(img_path)
    # img_resize = op_img.resize((224, 224))
    # img2arr = img_to_array(img_resize) / 255.0
    # img_reshape = img2arr.reshape(1, 224, 224, 3)
    # return img_reshape
    
    image = Image.open(img_path)
    image = image.resize((224, 224))  # Resize the image to match the input size of the model
    image = image.convert('RGB')
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add an extra dimension to match the model's input shape
    
    return image

# def predict_result(predict):
#     pred = model.predict(predict)
#     return np.max(pred[0]) * 100