import cv2

class ExeptionError(Exception):
    pass

def validate_video(path):
    video = cv2.VideoCapture(path)

    if not video.isOpened():
        raise ExeptionError("Could not open the video fil or find the device to connect.")
    
    return video

def open_camera(path_to_device):

    video = validate_video(path_to_device)
    
    win_name = "Video Stream"
    cv2.namedWindow(win_name)
    
    while True:
        has_frame, frame = video.read()

        if not has_frame:
            break

        frame = cv2.flip(frame, 1)

        cv2.imshow(win_name, frame)
        key = cv2.waitKey(0)

        if key == ord("Q") or key == ord("q") or key == 27:
            break

    video.release()
    cv2.destroyAllWindows()
