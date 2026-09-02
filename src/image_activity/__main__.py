import cv2
import sys

from pathlib import Path

# Configuration where to load and save the image relative to
# the main project directory.
IMAGE_PATH = "assets/kelpie.jpg"
IMAGE_DEST = "saved_image.png"

print(f"[!] Loading image at {IMAGE_PATH}...")
root_path = Path(__file__).resolve().parent.parent.parent

# Attempts to load an image from the IMAGE_PATH variable.
image = cv2.imread(root_path / IMAGE_PATH)

# imread may return None so we need to throw an error if it happens.
if image is None:
    print(f"[x] Failed to load image at: {IMAGE_PATH}!")
    sys.exit(1)

# Spawns a new window with an image in its absolute size.
cv2.imshow("Test Image", image)

# Waits for any key to be pressed in order to destroy the window.
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writes the loaded image into the IMAGE_DEST variable.
print("[/] Saved image at saved_image.png")
cv2.imwrite(root_path / "saved_image.png", image)
