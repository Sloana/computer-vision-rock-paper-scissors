import cv2
import time
import keras
from keras.models import load_model
import numpy as np
time.time()
model = load_model('C:/Users/laura/OneDrive/Desktop/Computer Vision/keras_model.h5')

def get_computer_choice():
    cap = cv2.VideoCapture(0)
    time.time()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    rps=["Rock","Paper","Scissors","Nothing"]
    while True: 
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
            print(f"Computer Choose{get_prediction()}")
        
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return print_winner()
def get_user_choice():
    user_choice=input("Enter a choice")
    return user_choice
def get_winner(computer_choice,user_choice):

    if computer_choice=="Rock":
        if user_choice=="Scissors":
            winner="computer"
        elif user_choice=="Paper":
            winner="user"
        else:
            winner="tied"
    elif computer_choice=="Scissors":
        if user_choice=="Paper":
            winner="computer"
        elif user_choice=="Rock":
            winner="user"
        else:
             winner="tied"
    elif computer_choice=="Paper":
        if user_choice=="Rock":
            winner="computer"
        elif user_choice=="Scissors":
            winner="user"
        else:
             winner="tied"
    if winner=="user":
        print("You won!")
    elif winner=="computer":
        print("You lost!")
    else:
        print("It is a tie!")
    return winner


def play():
    computer_wins=0
    user_wins=0

    rounds_played=0

    while computer_wins <= 3 or user_wins <= 3:
        rounds_played+=1

        if get_winner(get_computer_choice(),get_user_choice())=="computer":
            computer_wins+=1
        elif get_winner(get_computer_choice(),get_user_choice())=="user":
            user_wins+=1
        else:
            print("none of them win")
 
     

play()

