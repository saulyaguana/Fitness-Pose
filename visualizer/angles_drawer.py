import cv2

TEXT_COLOR = (0, 255, 0)

def draw_angles(frame, angles):
    
    for point, angle in angles:
        cv2.putText(
            frame,
            str(int(angle)),
            (point.x - 25, point.y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            TEXT_COLOR,
            2,
            cv2.LINE_AA
        )

    return frame