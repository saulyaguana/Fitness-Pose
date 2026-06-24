import cv2

LINE_COLOR = "#fcba03"
POINT_COLOR = "#5203fc"

def draw_landmarks(frame, body):
    # Left arm
    cv2.line(
        frame,
        (body.left_shoulder.x, body.left_shoulder.y),
        (body.left_elbow.x, body.left_elbow.y),
        LINE_COLOR,
        2,
        cv2.LINE_AA
    )

    cv2.line(
        frame,
        (body.left_elbow.x, body.left_elbow.y),
        (body.left_wrist.x, body.left_wrist.y),
        LINE_COLOR,
        2,
        cv2.LINE_AA
    )

    # Right arm
    cv2.line(
        frame,
        (body.right_shoulder.x, body.right_shoulder.y),
        (body.right_elbow.x, body.right_elbow.y),
        LINE_COLOR,
        2,
        cv2.LINE_AA
    )

    cv2.line(
        frame,
        (body.right_elbow.x, body.right_elbow.y),
        (body.right_wrist.x, body.right_wrist.y),
        LINE_COLOR,
        2,
        cv2.LINE_AA
    )

    # Shoulder to shoulder
    cv2.line(
        frame,
        (body.left_shoulder.x, body.left_shoulder.y),
        (body.right_shoulder.x, body.right_shoulder.y),
        LINE_COLOR,
        2,
        cv2.LINE_AA
    )

    # Points
    points = [
        body.left_shoulder,
        body.left_elbow,
        body.left_wrist,
        body.right_shoulder,
        body.right_elbow,
        body.right_wrist,
        body.nose
    ]

    for point in points:
        cv2.circle(
            frame,
            (point.x, point.y),
            3,
            POINT_COLOR,
            -1
        )

    return frame