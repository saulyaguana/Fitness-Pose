import math
import numpy as np

def compute_angle(v1, v2):
    # Unit vector
    v1u = v1 / np.linalg.norm(v1)
    # Unit vector
    v2u = v2 / np.linalg.norm(v2)
    # Compute the angle between the two unit vectors
    angle_deg = np.arccos(np.dot(v1u, v2u)) * 180 / math.pi

    return angle_deg