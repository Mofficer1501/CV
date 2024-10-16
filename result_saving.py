import numpy as np
import pandas as pd

def save_point_cloud(point_cloud, filename='output.ply'):
    # Сохранение облака точек в формате PLY
    with open(filename, 'w') as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write(f"element vertex {len(point_cloud)}\n")
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("end_header\n")
        for point in point_cloud:
            f.write(f"{point[0]} {point[1]} {point[2]}\n")

def save_camera_trajectory(camera_trajectory, filename='trajectory.csv'):
    df = pd.DataFrame(camera_trajectory, columns=['position_x', 'position_y', 'position_z', 'orientation_x', 'orientation_y', 'orientation_z'])
    df.to_csv(filename, index=False)
