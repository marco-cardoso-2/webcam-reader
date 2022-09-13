import cv2

from logger import LOGGER


class WebcamReader:
    """
    This script was based on the version available at
    https://www.geeksforgeeks.org/extract-video-frames-from-webcam-and-save-to-images-using-python/
    """

    def __init__(self):
        self.video_capture = self.get_video_capture()

    def get_camera_indexes(self):
        # checks the first 10 indexes.
        index = 0
        arr = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
            i -= 1
        return arr

    def start(self):

        while True:
            try:
                 self.read_video_capture_frame()
            except KeyboardInterrupt:
                break

        self.video_capture.release()
        cv2.destroyAllWindows()

    def get_video_capture(self) -> cv2.VideoCapture:

        video_indexes = self.get_camera_indexes()

        video_capture = cv2.VideoCapture(video_indexes[0])
        if not video_capture.isOpened():
            raise IOError("Cannot open webcam")

        return video_capture

    def read_video_capture_frame(self):
        ret, frame = self.video_capture.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            raise KeyboardInterrupt()
        return frame


if __name__ == "__main__":
    webcam_reader = WebcamReader()
    webcam_reader.start()
