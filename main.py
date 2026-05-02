import argparse
import time

from utils import to_grayscale, convolve, load_images, blur_score, find_duplicates, show_duplicate_pair, format_time


def main(folder):
    start_time = time.time()
    images = load_images(folder)
    print(f"\n Total images in memory: {len(images)}")
    duplicates = find_duplicates(images)
    print("\n Duplicates images found::\n")
    print(len(duplicates))
    """
    matplot display of duplicate images side by side
    for a, b, d in duplicates:
        print(f"{a} <-> {b} | distance: {d:.2f}")
        show_duplicate_pair(images[a], images[b], a, b, d)
    """
    end_time = time.time()
    time_taken = format_time(end_time - start_time)
    print(f"\n total time taken : {time_taken} seconds")

if __name__ == "__main__":
    folder = input("Enter image folder path: ").strip()
    main(folder)

