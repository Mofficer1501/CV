import open3d as o3d
import numpy as np
import cv2
import os

# Папка с изображениями
image_folder = 'site_capture'

# Считываем изображения
images = []
image_names = os.listdir(image_folder)
for image_name in image_names:
    img = cv2.imread(os.path.join(image_folder, image_name))
    images.append(img)


# Преобразование панорам в фрагменты (если необходимо)
def extract_patches(img):
    # Реализуйте вашу логику извлечения фрагментов из панорамы
    return [img]  # На выходе должны быть фрагменты


# Список найденных фрагментов
fragments = []
for img in images:
    fragments.extend(extract_patches(img))

# Параметры камеры
focal_length = 7.2  # Фокусное расстояние
camera_matrix = np.array([[focal_length, 0, img.shape[1] // 2],
                          [0, focal_length, img.shape[0] // 2],
                          [0, 0, 1]])

# Создание облака точек
points = []
colors = []
for fragment in fragments:
    # Извлечение признаков
    # Это место, где можно применять OpenCV для извлечения или сопоставления ключевых точек
    keypoints, descriptors = cv2.ORB_create().detectAndCompute(fragment, None)

    # Обработка ключевых точек и создание облака точек

# Создание 3D облака точек
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector(colors)

# Визуализация облака точек
o3d.visualization.draw_geometries([point_cloud])

# Сохранение облака точек в формате PLY
o3d.io.write_point_cloud("output.ply", point_cloud)

# Генерация траектории камеры
camera_trajectory = []
for i, img in enumerate(images):
    # Позиционирование и углы для каждой картинки
    camera_position = [0, 0, 0]  # Ваша логика для определения позиций
    camera_orientation = [0, 0, 0]  # Ваша логика для определения ориентации
    camera_trajectory.append([camera_position, camera_orientation])

# Сохранение траектории в CSV
import pandas as pd

camera_df = pd.DataFrame(camera_trajectory, columns=["Position", "Orientation"])
camera_df.to_csv("camera_trajectory.csv", index=False)