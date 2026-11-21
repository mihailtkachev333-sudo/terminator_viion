from frame_source import frame_source
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2

model = YOLO("yolo11n.pt") #загружаем модель 

fs = frame_source()


cv2.namedWindow("Video", cv2.WINDOW_NORMAL) #создаем окно для отображения видео 
cv2.resizeWindow("Video", 1280, 720) #изменяем размер окна для отображения видео

try: # пытался получить кадр с видеокамеры, если не получилось, то выкидываем ошибку
    for frame in fs.frames():
        results = model(frame)
        
        annotator = Annotator(frame, line_width=1)
        for box in results[0].boxes:
            class_id = int(box.cls.item())
            label = f"{results[0].names[class_id]} {box.conf.item():.2f}"
            annotator.box_label(box.xyxy[0].tolist(), label, color=(0, 0, 255))

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1) # промежуток паузы между кадрами в милисеках в ожиданнии нажатия клавиши ии считывает нажатия клавиатуры
        if key == ord('v'): # переводим клавишу в код
            break
        
finally:
    fs.release()