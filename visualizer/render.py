from visualizer.points_drawer import draw_points
from visualizer.lines_drawer import draw_lines
from visualizer.angles_drawer import draw_angles
from visualizer.counter_drawer import draw_counter
from visualizer.metrics_drawer import draw_metrics

def render(frame, exercise, body):
    draw_config = exercise.get_draw_config(body)

    frame = draw_lines(
        frame,
        draw_config["connections"]
    )

    frame = draw_points(
        frame,
        draw_config["points"]
    )

    frame = draw_angles(
        frame,
        draw_config["angles"]
    )

    frame = draw_counter(
        frame,
        exercise.get_repetitions()
    )

    frame = draw_metrics(
        frame,
        exercise.metrics
    )

    return frame