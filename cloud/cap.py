import cv2
from deep import run
import state
import time

caps = {}


vedio_path="http://192.168.43.59:8080/video"
cap = cv2.VideoCapture(vedio_path)
video_avai = True
if not cap.isOpened():
    video_avai = False
    print('Failed to open the camera')

def grasp_cap():
    if not video_avai:
        return
    while True:
        ret, frame = cap.read()
        caps['cap'] = frame
        if not ret:
            print('read image failed')
            return;
            

def deep_loop():
    if not video_avai:
        return
    while True:
        frame = caps['cap']
        shape = frame.shape

        # 截取正中心方形区域
        y, x = shape[0], shape[1]
        pad = y
        x_center = int(x/2)
        x_start = x_center - int(pad/2)
        x_end = x_start + pad
        crop = frame[:,x_start:x_end,:]
        crop = cv2.resize(crop, dsize=(192,192))
        crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
        state.state.deep_state = run.run_one(crop)
    
