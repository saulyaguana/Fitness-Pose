from core.landmarks import Point, BodyLandmarks
import cv2
import numpy as np
import mediapipe as mp

def get_landmark_points(landmarks, landmark_point, width, height):
    x = int(landmarks.landmark[landmark_point].x * width)
    y = int(landmarks.landmark[landmark_point].y * height)

    return np.array([x, y])


def create_pose_detector():
    return mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

def detect_pose(frame, pose):

    height, width = frame.shape[:2]

    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks is None:
        return None
        
    # nose
    nose = results.pose_landmarks.landmark[0]

    # Left shoulder
    l_shoulder = results.pose_landmarks.landmark[11]

    # Right shoulder
    r_shoulder = results.pose_landmarks.landmark[12]

    # left elbow
    l_elbow = results.pose_landmarks.landmark[13]

    # Right elbow
    r_elbow = results.pose_landmarks.landmark[14]

    # Left wrist
    l_wrist = results.pose_landmarks.landmark[15]

    # Right wrist
    r_wrist = results.pose_landmarks.landmark[16]

    # Left hip
    l_hip = results.pose_landmarks.landmark[23]

    # Right hip
    r_hip = results.pose_landmarks.landmark[24]

    # Left knee
    l_knee = results.pose_landmarks.landmark[25]

    # Right knee
    r_knee = results.pose_landmarks.landmark[26]

    # Left ankle
    l_ankle = results.pose_landmarks.landmark[27]

    # Right ankle
    r_ankle = results.pose_landmarks.landmark[28]

        

    body = BodyLandmarks(
        right_ankle = Point(
            x = int(r_ankle.x * width),
            y = int(r_ankle.y * height)
        ),
        left_ankle = Point(
            x = int(l_ankle.x * width),
            y = int(l_ankle.y * height)
        ),
        right_knee = Point(
            x = int(r_knee.x * width),
            y = int(r_knee.y * height)
        ),
        left_knee = Point(
            x = int(l_knee.x * width),
            y = int(l_knee.y * height)
        ),
        right_hip = Point(
            x = int(r_hip.x * width),
            y = int(r_hip.y * height)
        ),
        left_hip = Point(
            x = int(l_hip.x * width),
            y = int(l_hip.y * height)
        ),
        left_wrist = Point(
            x = int(l_wrist.x * width),
            y = int(l_wrist.y * height)
        ),
        left_shoulder = Point(
            x = int(l_shoulder.x * width),
            y = int(l_shoulder.y * height)
        ),
        right_shoulder = Point(
            x = int(r_shoulder.x * width),
            y = int(r_shoulder.y * height)
        ),
        nose = Point(
            x = int(nose.x * width),
            y = int(nose.y * height)
        ),
        right_wrist = Point(
            x = int(r_wrist.x * width),
            y = int(r_wrist.y * height)
        ),
        right_elbow = Point(
            x= int(r_elbow.x * width),
            y = int(r_elbow.y * height)
        ),
        left_elbow = Point(
            x = int(l_elbow.x * width),
            y = int(l_elbow.y * height)
        )
    )
    return body