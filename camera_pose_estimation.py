import cv2
import numpy as np

def estimate_camera_pose(image, keypoints, object_points):
    focal_length = 6.7
    center = (image.shape[1] / 2, image.shape[0] / 2)
    camera_matrix = np.array([[focal_length, 0, center[0]],
                               [0, focal_length, center[1]],
                               [0, 0, 1]], dtype='float32')

    if len(keypoints) != len(object_points):
        raise ValueError("Количество 2D ключевых точек должно совпадать с количеством 3D объектных точек")

    keypoints = np.array(keypoints, dtype='float32')
    object_points = np.array(object_points, dtype='float32')

    success, rotation_vector, translation_vector = cv2.solvePnP(object_points, keypoints, camera_matrix, None)

    if not success:
        raise RuntimeError("Не удалось оценить позу камеры")

    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    orientation = cv2.decomposeProjectionMatrix(np.hstack((rotation_matrix, translation_vector)))[6]

    position = translation_vector.flatten()
    orientation = orientation.flatten()

    return {"position": position, "orientation": orientation}