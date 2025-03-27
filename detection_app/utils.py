import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load your model
model_path = os.path.join(os.path.dirname(__file__), 'shopLiftingDetector.h5')
model = load_model(model_path)

def extract_frames(video_path, frame_count=8):
    """Extract frames from video for prediction"""
    cap = cv2.VideoCapture(video_path)
    frames = []
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    for i in np.linspace(0, total_frames - 1, frame_count).astype(int):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = cap.read()
        if success:
            frame = cv2.resize(frame, (180, 180))
            frames.append(frame)
    cap.release()
    return frames

def predict_shoplifting(video_path):
    """Predict shoplifting from video"""
    frames = extract_frames(video_path)
    predictions = []
    
    for frame in frames:
        # Preprocess the frame
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = image.img_to_array(img)
        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)
        
        # Make prediction
        pred = model.predict(img)[0][0]
        predictions.append(pred)
    
    # Average predictions across frames
    avg_prediction = np.mean(predictions)
    is_shoplifting = avg_prediction > 0.5  # Threshold can be adjusted
    
    return {
        'is_shoplifting': bool(is_shoplifting),
        'confidence': float(avg_prediction),
        'frame_predictions': [float(p) for p in predictions]
    }