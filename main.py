import time
from utils import load_images, find_duplicates


def main(folder):
    start = time.time()

    images = load_images(folder)
    print(f"\nTotal images in memory: {len(images)}")

    duplicates = find_duplicates(images)

    print("\nDuplicates found:\n")
    print(len(duplicates))

    for a, b, d in duplicates:
        print(f"{a} <-> {b} | distance: {d}")

    end = time.time()
    print(f"\nTotal time: {end - start:.2f} sec")


if __name__ == "__main__":
    folder = input("Enter image folder path: ").strip()
    main(folder)