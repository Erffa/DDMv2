import cv2
import time
from kafka import KafkaProducer


producer = KafkaProducer(
	bootstrap_servers="10.3.121.112:6667", 
	api_version=(0, 10, 1))
print("kafka producer : connection success")

cap = cv2.VideoCapture('http://10.4.108.33/mjpg/video.mjpg')
print(f"video-capture is opened : {cap.isOpened()}")

while(cap.isOpened()):
    print("loop start")
    start_time = time.time()

    ret, frame = cap.read()
    is_success, im_buf_arr = cv2.imencode(".jpg", frame)

    byte_im = im_buf_arr.tobytes()
    
    producer.send("video", byte_im)
    pass