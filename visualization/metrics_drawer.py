import cv2

def draw_metrics(frame, body, metrics):
    cv2.putText(
        frame,
        str(int(metrics.left_elbow_angle)),
        (body.left_elbow.x - 25, body.left_elbow.y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        frame,
        str(int(metrics.right_elbow_angle)),
        (body.right_elbow.x - 25, body.right_elbow.y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        frame,
        str(int(metrics.left_shoulder_angle)),
        (body.left_shoulder.x - 25, body.left_shoulder.y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        2,
        cv2.LINE_AA
    )

    cv2.putText(
        frame,
        str(int(metrics.right_shoulder_angle)),
        (body.right_shoulder.x - 25, body.right_shoulder.y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        2,
        cv2.LINE_AA
    )

    return frame