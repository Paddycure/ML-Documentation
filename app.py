import os
# import cv2
import numpy as np
import tensorflow_hub as hub

from tensorflow.keras.models import load_model
from flask import Flask, request, render_template

from preprocessing import preprocessing_image
from description import description
from suggestion import suggestion

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = 'static/uploaded'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'jfif'])
class_names = ['Bacterial Blight', 'Brown Spot', 'Healthy', 'Hispa', 'Leaf Blast', 'Leaf Smut', 'Tungro']  # Replace with your own class names

# # Load Model dengan GPU
# model = load_model(('models/Merged_Model_95-84.h5'),
#                    custom_objects={'KerasLayer':hub.KerasLayer})

# Load Model TANPA GPU
model = load_model(('models/model-mix.h5'),
                   compile=False,
                   custom_objects={'KerasLayer':hub.KerasLayer})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template("index.html")


@app.route('/predicton', methods=['GET','POST'])
def predict_image_file():
    try:
        if request.method == 'GET':
            return render_template('index.html')

        if request.method == 'POST':
            if 'file' not in request.files:
                return render_template('index.html')
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = file.filename.replace(' ','_')
                dest = 'static/uploaded/'+filename
                file.stream.seek(0)
                file.save(dest)
                file.stream.seek(0)
                image = preprocessing_image(dest)
                image = preprocessing_image(request.files['file'].stream)
                
                predictions = model.predict(image)
                predicted_class = class_names[np.argmax(predictions[0])]
                confidence = round(np.max(predictions[0]) * 100)
                
                desc = description(predicted_class)
                suggest = suggestion(predicted_class)
                
                # predict from model
                # img = cv2.imread(dest)
                # # h, w, _ = img.shape
                # (h, w) = img.shape[:2]
                
                # preds = model.predict(image)[0]
                # (startX, startY, endX, endY) = preds
                
                # startX = int(startX * w)
                # startY = int(startY * h)
                # endX = int(endX * w)
                # endY = int(endY * h)
                
                # resp = model(image)

                # # get the output of the prediction
                # # iterate over boxes, class_index and score list
                # for boxes, classes, scores in zip(resp['detection_boxes'].numpy(), resp['detection_classes'], resp['detection_scores'].numpy()):
                #     for box, cls, score in zip(boxes, classes, scores): # iterate over sub values in list
                #         if score > 0.6: # we are using only detection with confidence of over 0.8
                #             ymin = int(box[0] * h)
                #             xmin = int(box[1] * w)
                #             ymax = int(box[2] * h)
                #             xmax = int(box[3] * w)
                            
                #             # draw on image
                #             cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (128, 0, 128), 2)
                #             cv2.putText(dest, predicted_class, (int(ymin), int(xmin - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 0, 128), 2)

                # cv2.rectangle(img, (startX, startY), (endX, endY), (128, 0, 128), 2)
                # cv2.putText(dest, predicted_class, (int(startX), int(startY - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 0, 128), 2)
                
                # convert back to bgr and save image
                # image_result = cv2.imwrite(dest, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                
                return render_template('result.html', 
                                    #    image_result=image_result,
                                       prediction=predicted_class,
                                       confidence=confidence,
                                       description=desc,
                                       suggestion=suggest)
    
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    
if __name__ == '__main__':
    app.run(port=9000, debug=True)
