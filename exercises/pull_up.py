import time
from exercises.base_exercise import BaseExercise
from core.metrics import joint_angle, calculate_rom, calculate_rep_time, calculate_cadence
from core.metrics_models import PullUpMetrics

class PullUp(BaseExercise):
    def __init__(self):
        self.counter = 0
        self.is_up = False
        self.metrics = PullUpMetrics()
        self.initial_nose_y = None

        self.min_elbow_angle = 180
        self.max_elbow_angle = 0
        self.rep_start_time = 0
        self.session_start_time = 0

        self.rom_history = []
        self.rep_time_history = []
        self.cadence_history = []

    def get_draw_config(self, body):
        return {
            "points": [
                body.left_shoulder,
                body.left_elbow,
                body.left_wrist,

                body.right_shoulder,
                body.right_elbow,
                body.right_wrist,

                body.nose
            ],
            "connections": [
                (body.left_shoulder, body.left_elbow),
                (body.left_elbow, body.left_wrist),
                
                (body.right_shoulder, body.right_elbow),
                (body.right_elbow, body.right_wrist),

                (body.left_shoulder, body.right_shoulder)
            ],
            "angles": [
                (body.left_elbow, self.metrics.left_elbow_angle),
                (body.right_elbow, self.metrics.right_elbow_angle),
                
                (body.left_shoulder, self.metrics.left_shoulder_angle),
                (body.right_shoulder, self.metrics.right_shoulder_angle)
            ]
        }

    def get_metrics(self, body):
        left_elbow_angle = joint_angle(
            body.left_shoulder,
            body.left_elbow,
            body.left_wrist
        )

        right_elbow_angle = joint_angle(
            body.right_shoulder,
            body.right_elbow,
            body.right_wrist
        )

        left_shoulder_angle = joint_angle(
            body.left_elbow,
            body.left_shoulder,
            body.right_shoulder
        )

        right_shoulder_angle = joint_angle(
            body.right_elbow,
            body.right_shoulder,
            body.left_shoulder
        )

        # self.metrics = {
        #     "left_elbow_angle": left_elbow_angle,
        #     "right_elbow_angle": right_elbow_angle,
        #     "left_shoulder_angle": left_shoulder_angle,
        #     "right_shoulder_angle": right_shoulder_angle,
        # }
        self.metrics.left_elbow_angle = left_elbow_angle
        self.metrics.right_elbow_angle = right_elbow_angle
        self.metrics.left_shoulder_angle = left_shoulder_angle
        self.metrics.right_shoulder_angle = right_shoulder_angle

        return self.metrics
    
    def process(self, body):

        if self.initial_nose_y == None:
            self.initial_nose_y = body.nose.y

        metrics = self.get_metrics(body)

        left_elbow_angle = metrics.left_elbow_angle
        right_elbow_angle = metrics.right_elbow_angle

        left_shoulder_angle = metrics.left_shoulder_angle
        right_shoulder_angle = metrics.right_shoulder_angle

        UP_ANGLE_MIN = 7
        UP_ANGLE_MAX = 25

        SHOULDER_ANGLE_MIN = 128
        SHOULDER_ANGLE_MAX = 145

        is_up_position = (

            left_elbow_angle >= UP_ANGLE_MIN and
            left_elbow_angle <= UP_ANGLE_MAX and

            right_elbow_angle >= UP_ANGLE_MIN and
            right_elbow_angle <= UP_ANGLE_MAX and

            left_shoulder_angle >= SHOULDER_ANGLE_MIN and
            left_shoulder_angle <= SHOULDER_ANGLE_MAX and

            right_shoulder_angle >= SHOULDER_ANGLE_MIN and
            right_shoulder_angle <= SHOULDER_ANGLE_MAX and

            body.nose.y <= self.initial_nose_y + 60

        )

        DOWN_ANGLE_THRESHOLD = 160

        is_down_position = (
            left_elbow_angle >= DOWN_ANGLE_THRESHOLD and
            right_elbow_angle >= DOWN_ANGLE_THRESHOLD
        )

        if is_up_position:
            self.is_up = True
        elif is_down_position and self.is_up:
            self.counter += 1
            self.is_up = False

            self.metrics.rom = calculate_rom(self.min_elbow_angle, self.max_elbow_angle)
            self.metrics.rep_time = calculate_rep_time(self.rep_start_time, time.time())
            self.metrics.cadence = calculate_cadence(self.get_repetitions(), time.time() - self.session_start_time)

            self.rom_history.append(self.metrics.rom)
            self.rep_time_history.append(self.metrics.rep_time)
            self.cadence_history.append(self.metrics.cadence)

    def get_repetitions(self):
        return self.counter
    
    def get_summary(self):
        average_rom = (
            sum(self.rom_history) / len(self.rom_history)
            if self.rom_history else 0
        )

        average_rep_time = (
            sum(self.rep_time_history) / len(self.rep_time_history)
            if self.rep_time_history else 0
        )

        average_cadence = (
            sum(self.cadence_history) / len(self.cadence_history)
            if self.cadence_history else 0
        )

        return {
            "Excercise":  "Pull Ups",
            "Repetitions": self.get_repetitions(),
            "average_rom": average_rom,
            "average_rep_time": average_rep_time,
            "average_cadence": average_cadence
        }