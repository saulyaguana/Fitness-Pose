import cv2

POINT_COLOR = (3, 186, 252)
POINT_RADIUS = 4

def draw_points(frame, points):
    
    for point in points:
        cv2.circle(
            frame,
            (point.x, point.y),
            POINT_RADIUS,
            POINT_COLOR,
            -1
        )
 
    return frame
