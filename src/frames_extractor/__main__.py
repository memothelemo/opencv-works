import cv2
import os
import pathlib
import sys

from pathlib import Path

# Opens the captured video from the specified path.
capture = cv2.VideoCapture("input.mp4")

if not capture.isOpened():
    print("[x] Failed to load input.mp4 file!")
    sys.exit(1)

print("[!] Extracting frames from input.mp4...")

# We need to get the captured device's width, height and its FPS for video encoding soon.
cap_frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_frame_fps = int(capture.get(cv2.CAP_PROP_FPS))

# Create output folder for frames
output_folder = Path(__file__).parent.parent.parent / "extracted_frames"
os.makedirs(output_folder, exist_ok=True)

# Extract every frame from the video
extracted_frames = 0

while True:
    ret, frame = capture.read()

    # The video capture stream is exhausted if it returns false.
    if not ret: break

    frame_file_name = output_folder / f"frame_{extracted_frames:04d}.png"
    cv2.imwrite(frame_file_name, frame)

    extracted_frames += 1

capture.release()
print(f"[/] Successfully extracted {extracted_frames} frame(s).")
