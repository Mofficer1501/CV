import numpy as np

def filter_noise(point_cloud, threshold=0.05):
    # Применяем фильтрацию шума, используя пороговое значение
    # Удаляем точки, которые находятся слишком близко друг к другу
    filtered_points = []
    for point in point_cloud:
        # Проверяем расстояние до остальных точек
        if all(np.linalg.norm(point - other_point) > threshold for other_point in filtered_points):
            filtered_points.append(point)

    return np.array(filtered_points)
