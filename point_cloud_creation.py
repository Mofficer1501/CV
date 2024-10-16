import numpy as np
import open3d as o3d

def create_point_cloud(keypoints):
    points = np.array([kp.pt for kp in keypoints])
    return points

def visualize_point_cloud(point_cloud):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud)
    o3d.visualization.draw_geometries([pcd])