# numpy-smart-image-cleaner
NumPy Smart Image Cleaner — Detect and remove duplicate images using vector similarity.

Example:

Over time, image folders accumulate duplicate and near-duplicate files, leading to wasted storage and disorganized data. Manual cleanup is slow and inefficient.

This project automates duplicate detection using image processing and numerical similarity techniques.

- Load images from a local folder
- Convert images to grayscale
- Resize images for uniform processing
- Convert images into numerical vectors
- Detect duplicates using Euclidean distance
- (Optional) Visualize duplicate pairs using Matplotlib

Tech-Stack
- Python
- NumPy
- OpenCV
- Matplotlib