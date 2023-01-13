import cv2
import time
import keras
from keras.models import load_model
import numpy as np
time.time()
model = load_model('C:/Users/laura/OneDrive/Desktop/Computer Vision/keras_model.h5')
cap = cv2.VideoCapture(0)
time.time()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
rps=["Rock","Paper","Scissors","Nothing"]
print("cam")
i=5
while i>0: 
    print("camera")
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    def get_prediction():
        prediction = model.predict(data)
        pred=rps[np.argmax(prediction)]
        return pred
    def print_winner():
        print(f"Winner is:{get_prediction()}")
    print_winner()
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
          
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
