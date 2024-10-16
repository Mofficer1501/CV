import cv2

def extract_patches(image, patch_size=(1024, 1024)):
    patches = []
    for y in range(0, image.shape[0], patch_size[0]):
        for x in range(0, image.shape[1], patch_size[1]):
            patch = image[y:y + patch_size[0], x:x + patch_size[1]]
            if patch.shape[0] == patch_size[0] and patch.shape[1] == patch_size[1]:
                patches.append(patch)
    return patches

def detect_keypoints_on_patch(patch):
    sift = cv2.SIFT_create()
    keypoints = sift.detect(patch, None)
    return keypoints