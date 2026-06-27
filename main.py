import cv2

from exercises.pull_up import PullUp
from vision.frame_processor import stream_body_landmarks
from visualizer.render import render
# from visualization.render import render

VIDEO_PATH = "C:/Users/sauly/Desktop/video_samples/pull_ups.mp4"

def main():
    exercise = PullUp()

    for frame, body in stream_body_landmarks(VIDEO_PATH):
        exercise.process(body)

        frame = render(frame, exercise, body)

        cv2.imshow("Pull Ups", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()