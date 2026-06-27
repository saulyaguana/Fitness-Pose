import cv2

def draw_counter(frame, repetitions):
    
    frame[20:80, 0:80] = 0

    cv2.putText(
        frame,
        str(repetitions),
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2,
        cv2.LINE_AA
    )

    return frame