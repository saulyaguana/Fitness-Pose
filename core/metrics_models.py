from dataclasses import dataclass

@dataclass
class ExerciseMetrics:
    pass

@dataclass
class PullUpMetrics(ExerciseMetrics):
    left_elbow_angle: float = 0.0
    right_elbow_angle: float = 0.0

    left_shoulder_angle: float = 0.0
    right_shoulder_angle: float = 0.0

    rom: float = 0.0

    rep_time: float = 0.0

    cadence: float = 0.0