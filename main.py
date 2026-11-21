from frame_source import frame_source
from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt") #загружаем модель 

fs = frame_source()


cv2.namedWindow("Video", cv2.WINDOW_NORMAL) #создаем окно для отображения видео 
cv2.resizeWindow("Video", 1280, 720) #изменяем размер окна для отображения видео

try: # пытался получить кадр с видеокамеры, если не получилось, то выкидываем ошибку
    for frame in fs.frames():
        results = model(frame)
        frame = results[0].plot(line_width=1, ) # рисуем рамки на кадре
        cv2.imshow("Video", frame)
        key = cv2.waitKey(1) # промежуток паузы между кадрами в милисеках в ожиданнии нажатия клавиши ии считывает нажатия клавиатуры
        if key == ord('v'): # переводим клавишу в код
            break
        
finally:
    fs.release()