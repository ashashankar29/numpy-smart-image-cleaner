import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_image_files(folder):
    valid_ext = {".jpg", ".jpeg", ".png"}
    print("Current working directory:", os.getcwd())
    print("files in image folder")

    files = os.listdir(folder)

    return [
        f for f in files
        if os.path.splitext(f)[1].lower() in valid_ext
    ]

def load_images(folder):
    images ={}
    image_files = get_image_files(folder)
    print(f"Found {len(image_files)} image files\n")

    for f in image_files:
        path = os.path.join(folder, f)
        img = cv2.imread(path)
        if img is not None:
            images[f] = img
    return images

def to_grayscale(img):
    return np.dot(img[..., :3], [0.299, 0.587, 0.114])

def blur_score(gray_image):
    laplacian_kernel = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1,  0]
    ])
    lap = convolve(gray_image, laplacian_kernel)
    return lap.var()

def convolve(gray_image, lap_kernel):
    h, w = gray_image.shape
    kh, kw = lap_kernel.shape
    pad_h = kh//2
    pad_w = kw//2

    padded = np.pad(gray_image,((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    output = np.zeros_like(gray_image)
    for i in range (h):
        for j in range (w):
            region = padded[i:i+kh, j:j+kw]
            output[i,j] = np.sum(region * lap_kernel)

    return output

def find_duplicates(images):
    processed = {}

    #1. preprocess so it's easy to compare two images
    for name, img in images.items():
        proc = to_grayscale(img)
        vec = image_to_vector(proc)
        processed[name] = vec

    #2. compare all pairs
    names = list(processed.keys())
    duplicates = []

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            n1, n2 = names[i], names[j]
            dist = np.linalg.norm(processed[n1] - processed[n2])
            if dist < 100:
                duplicates.append((n1, n2, dist))
    return duplicates


def image_to_vector(img):
    #resizing image to gain speed.
    img = cv2.resize(img, (64, 64))


    return img.flatten()

def show_duplicate_pair(img1, img2, name_1, name_2, score):
    plt.figure(figsize=(10, 15))

    plt.subplot(1, 2, 1)
    plt.imshow(img1, cmap="gray")
    plt.title(name_1)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img2, cmap="gray")
    plt.title(name_2)
    plt.axis("off")

    plt.suptitle(f"Duplicate Pair | Distance: {score: .2f}")
    plt.show()


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 60 ) // 60)
    secs = seconds % 60
    if hours > 0:
        return f"{hours} hr {minutes} min {secs} sec"
    elif minutes > 0:
        return f"{minutes} min {secs:.2f}"
    else:
        return f"{secs:.2f}  sec"