import cv2

LINE_COLOR = (252, 3, 82)
LINE_WIDTH = 2

def draw_lines(frame, connections):
    
    for start, end in connections:
        cv2.line(
            frame,
            (start.x, start.y),
            (end.x, end.y),
            LINE_COLOR,
            LINE_WIDTH,
            cv2.LINE_AA
        )

    return frame
