from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class BodyLandmarks:
    nose: Point
    left_shoulder: Point
    right_shoulder: Point
    left_elbow: Point
    right_elbow: Point
    left_wrist: Point
    right_wrist: Point
    left_hip: Point
    right_hip: Point
    left_knee: Point
    right_knee: Point
    left_ankle: Point
    right_ankle: Point
