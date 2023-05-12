from keras.models import load_model
import numpy as np
import cv2
     

emotionModelPath = 'model/emotionModel.hdf5'  # fer2013_mini_XCEPTION.110-0.65
emotionClassifier = load_model(emotionModelPath, compile=False)
emotionTargetSize = emotionClassifier.input_shape[1:3]
emotions = {
    0: {
        "emotion": "Angry",
        "color": (193, 69, 42)
    },
    1: {
        "emotion": "Disgust",
        "color": (164, 175, 49)
    },
    2: {
        "emotion": "Fear",
        "color": (40, 52, 155)
    },
    3: {
        "emotion": "Happy",
        "color": (23, 164, 28)
    },
    4: {
        "emotion": "Sad",
        "color": (164, 93, 23)
    },
    5: {
        "emotion": "Suprise",
        "color": (218, 229, 97)
    },
    6: {
        "emotion": "Neutral",
        "color": (108, 72, 200)
    }
}
     

def frame_to_prid(x,y,h,w,img):
        grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        grayFace = grayFrame[y:y + h, x:x + w]
        
        grayFace = cv2.resize(grayFace, (emotionTargetSize))
    
        grayFace = grayFace.astype('float32')
        grayFace = grayFace / 255.0
        grayFace = (grayFace - 0.5) * 2.0
        grayFace = np.expand_dims(grayFace, 0)
        grayFace = np.expand_dims(grayFace, -1)
        emotion_prediction = emotionClassifier.predict(grayFace)
        emotion_probability = np.max(emotion_prediction)
        # print(emotion_prediction)
        # print(emotion_probability)
        emotion_label_arg = np.argmax(emotion_prediction)
        print(emotions[emotion_label_arg]['emotion'])
        print(emotion_label_arg)
        return str(emotion_label_arg)
     


     
