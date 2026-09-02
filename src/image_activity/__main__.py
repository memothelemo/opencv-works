import cv2
import sys

from pathlib import Path

IMAGE_PATH = "assets/kelpie.jpg"
IMAGE_DEST = "saved_image.png"

print(f"[!] Loading image at {IMAGE_PATH}...")
root_path = Path(__file__).resolve().parent.parent.parent

image = cv2.imread(root_path / IMAGE_PATH)
if image is None:
    print(f"[x] Failed to load image at: {IMAGE_PATH}!")
    sys.exit(1)

cv2.imshow("Test Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("[/] Saved image at saved_image.png")
cv2.imwrite("saved_image.png", image)
