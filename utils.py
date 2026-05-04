import os
from collections import defaultdict

import cv2
import numpy as np


def get_image_files(folder):
    valid_ext = {".jpg", ".jpeg", ".png"}
    files = os.listdir(folder)

    return [
        f for f in files
        if os.path.splitext(f)[1].lower() in valid_ext
    ]


def load_images(folder):
    images = {}
    image_files = get_image_files(folder)

    print(f"Found {len(image_files)} image files\n")

    for f in image_files:
        path = os.path.join(folder, f)
        img = cv2.imread(path)

        if img is None:
            print(f"⚠️ Failed to load: {f}")
            continue

        images[f] = img

    return images


# 🔥 pHash
def compute_phash(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (32, 32))

    dct = cv2.dct(np.float32(resized))
    dct_low = dct[:8, :8]

    median = np.median(dct_low)
    hash_bits = (dct_low > median).flatten()

    return hash_bits


def hamming_distance(h1, h2):
    return np.count_nonzero(h1 != h2)

def find_duplicates(images, threshold=10):
    hash_map = defaultdict(list)

    # 1. compute hashes
    for name, img in images.items():
        h = compute_phash(img)

        key = ''.join(['1' if x else '0' for x in h])
        hash_map[key].append(name)

    duplicates = []

    # 2. group duplicates
    for group in hash_map.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    duplicates.append((group[i], group[j], 0))

    return duplicates