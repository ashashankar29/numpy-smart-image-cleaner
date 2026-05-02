from utils import to_grayscale, convolve, load_images, blur_score, find_duplicates

def main():
    folder = "D:\\testData-forTestingProjects"
    images = load_images(folder)
    print(f"\n Total images in memory: {len(images)}")
    duplicates = find_duplicates(images)
    print("\n Duplicates images found::\n")
    print(len(duplicates))
    for a, b, d in duplicates:
        print(f"{a} <-> {b} | distance: {d:.2f}")



if __name__ == "__main__":
        main()

