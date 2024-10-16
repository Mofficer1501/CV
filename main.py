'''from image_preprocessing import read_images, convert_to_grayscale, apply_gaussian_blur, detect_keypoints
from patch_extraction import extract_patches, detect_keypoints_on_patch
from point_cloud_creation import create_point_cloud, visualize_point_cloud
from camera_pose_estimation import estimate_camera_pose
from noise_filtering import filter_noise
from result_saving import save_point_cloud, save_camera_trajectory

def main(image_folder):
    images = read_images(image_folder)
    all_keypoints = []
    camera_trajectory = []

    for img in images:
        gray_img = convert_to_grayscale(img)
        blurred_img = apply_gaussian_blur(gray_img)
        keypoints = detect_keypoints(blurred_img)
        all_keypoints.extend(keypoints)

        # Извлечение патчей и обнаружение ключевых точек на каждом патче
        patches = extract_patches(blurred_img)
        for patch in patches:
            patch_keypoints = detect_keypoints_on_patch(patch)
            all_keypoints.extend(patch_keypoints)

        # Оценка положения камеры 
        pose = estimate_camera_pose(img, keypoints)
        camera_trajectory.append(pose)

    # Создание облака точек и фильтрация шума
    point_cloud = create_point_cloud(all_keypoints)
    filtered_point_cloud = filter_noise(point_cloud)

    # Визуализация и сохранение результатов visualize_point_cloud(filtered_point_cloud)
    save_point_cloud(filtered_point_cloud)
    save_camera_trajectory(camera_trajectory)

if __name__ == "__main__":
    image_folder = '/Users/magomedmagomedov/PycharmProjects/CV/site_capture'''

from image_preprocessing import read_images, convert_to_grayscale, apply_gaussian_blur, detect_keypoints
from patch_extraction import extract_patches, detect_keypoints_on_patch
from point_cloud_creation import create_point_cloud, visualize_point_cloud
from camera_pose_estimation import estimate_camera_pose
from noise_filtering import filter_noise
from result_saving import save_point_cloud, save_camera_trajectory

def main(image_folder):
    images = read_images(image_folder)
    all_keypoints = []
    camera_trajectory = []

    for img in images:
        gray_img = convert_to_grayscale(img)
        blurred_img = apply_gaussian_blur(gray_img)
        keypoints = detect_keypoints(blurred_img)
        all_keypoints.extend(keypoints)

        patches = extract_patches(blurred_img)
        for patch in patches:
            patch_keypoints = detect_keypoints_on_patch(patch)
            all_keypoints.extend(patch_keypoints)

        pose = estimate_camera_pose(img, keypoints)
        camera_trajectory.append(pose)

    point_cloud = create_point_cloud(all_keypoints)
    filtered_point_cloud = filter_noise(point_cloud)

    visualize_point_cloud(filtered_point_cloud)
    save_point_cloud(filtered_point_cloud)
    save_camera_trajectory(camera_trajectory)

if __name__ == "__main__":
    image_folder = '/Users/magomedmagomedov/PycharmProjects/CV/site_capture'
    main(image_folder)
