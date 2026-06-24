from vision.camera import read_frame
from vision.pose_detector import detect_pose, create_pose_detector

def stream_body_landmarks(path):
    pose = create_pose_detector()

    for frame in read_frame(path):
        body = detect_pose(frame, pose)

        if body is None:
            continue

        yield frame, body