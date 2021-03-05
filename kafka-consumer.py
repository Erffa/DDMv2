from kafka import KafkaConsumer
from json import loads
import cv2
import numpy as np

consumer = KafkaConsumer(
    'video',
    bootstrap_servers="10.3.121.112:6667",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    consumer_timeout_ms=20000,
    api_version=(0, 10, 1))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

collection = []
for frame in consumer:

    frame = cv2.imdecode(np.float32(frame.value), cv2.COLOR_RGB2GRAY)
    #frame = cv2.imdecode(frame.value, cv2.IMREAD_COLOR)
    #frame = frame.value
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imwrite('face_image/{}.jpg'.format(time.time()), frame)
