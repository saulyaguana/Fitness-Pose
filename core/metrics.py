from core.geometry import compute_angle
from vision.frame_processor import stream_body_landmarks
import numpy as np

def joint_angle(point_a, point_b, point_c):
    A = np.array([point_a.x, point_a.y])
    B = np.array([point_b.x, point_b.y])
    C = np.array([point_c.x, point_c.y])

    vector_ba = A - B
    vector_bc = C - B

    angle = compute_angle(vector_ba, vector_bc)

    return angle