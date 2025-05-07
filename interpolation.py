import numpy as np
import cv2
import time

video = cv2.VideoCapture('video_test.mp4')
FPS = 60.

frame_idx = -1
while video.isOpened():

    now = time.time()
    frame_idx += 1
    ret, frame = video.read()
    if not ret:
        break
    # (opcional) processamento em frame
    wait_time = max(1,int((1/FPS - (time.time() - now)) * 1000))
    if frame_idx % 2 == 0:
        cv2.imshow('Video', frame)
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break
    elif cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break
    

video.release()
cv2.destroyAllWindows()