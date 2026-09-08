import cv2
import sys

# Opens the captured video from the specified path.
capture = cv2.VideoCapture("input.mp4")

if not capture.isOpened():
    print("[x] Failed to load input.mp4 file!")
    sys.exit(1)

print("[!] Generating mirrored video from input.mp4...")

# We need to get the captured device's width, height and its FPS for video encoding soon.
cap_frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_frame_fps = int(capture.get(cv2.CAP_PROP_FPS))

# Loads the MP4V codec
mp4v_codec = cv2.VideoWriter.fourcc(*"mp4v")

# Writer file stream for the recorded video
writer = cv2.VideoWriter(
    filename="output.mp4",
    fourcc=mp4v_codec,
    fps=cap_frame_fps,
    frameSize=(cap_frame_width, cap_frame_height)
)

while capture.isOpened():
    ret, frame = capture.read()

    # The video capture stream is exhausted if it returns false.
    if not ret: break

    # 1 means horizontal flip
    flipped_frame = cv2.flip(frame, 1)
    writer.write(flipped_frame)

writer.release()
print(f"[/] Saved mirror video at output.mp4")

capture.release()
