import cv2
class frame_source:
    def __init__(self, source=0):
        self.source = source
        self.capture = cv2.VideoCapture(self.source)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #устанавливаем ширину кадра
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) #устанавливаем высоту кадра

    def get_frame(self):
        ret, frame = self.capture.read()#ret bool работает какмера не работает # frame - это кадр который мы получаем
        if not ret:
            raise ValueError("не смогли получить кадр с видеокамеры")
        return frame

    def release(self):
        self.capture.release()

    def frames(self):
        while True:
            yield self.get_frame()
