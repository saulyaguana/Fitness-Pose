import cv2

TEXT_COLOR = (255, 255, 255)
BACKGROUND = (0, 0, 0)

def draw_metrics(frame, metrics):
    x = 10
    y = frame.shape[0] - 90

    cv2.rectangle(
        frame,
        (x - 5, y - 20),
        (230, frame.shape[0] - 10),
        BACKGROUND,
        -1
    )

    cv2.putText(
        frame,
        f"ROM: {metrics.rom:.1f}",
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        TEXT_COLOR,
        1,
        cv2.LINE_AA
    )

    cv2.putText(
        frame,
        f"Rep Time: {metrics.rep_time:.2f}s",
        (x, y + 22),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        TEXT_COLOR,
        1,
        cv2.LINE_AA
    )

    cv2.putText(
        frame,
        f"Cadence: {metrics.cadence:.2f}",
        (x, y + 44),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        TEXT_COLOR,
        1,
        cv2.LINE_AA
    )

    return frame