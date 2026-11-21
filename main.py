from frame_source import frame_source
from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt") #загружаем модель 

fs = frame_source() 
try: # пытался получить кадр с видеокамеры, если не получилось, то выкидываем ошибку
    for frame in fs.frames():
        results = model(frame)
        frame = results[0].plot() # рисуем рамки на кадре
        cv2.imshow("Video", frame)
        key = cv2.waitKey(1) # промежуток паузы между кадрами в милисеках в ожиданнии нажатия клавиши ии считывает нажатия клавиатуры
        if key == ord('v'): # переводим клавишу в код
            break
        
finally:
    fs.release()