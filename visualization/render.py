from visualization.landmarks_drawer import draw_landmarks
from visualization.metrics_drawer import draw_metrics
from visualization.counter_drawer import draw_counter

def render(frame, body, exercise):
    metrics = exercise.get_metrics(body)

    frame = draw_landmarks(frame, body)

    frame = draw_metrics(
        frame,
        body,
        metrics
    )

    frame = draw_counter(
        frame,
        exercise.get_repetitions()
    )

    return frame