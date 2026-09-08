import cv2
import sys

# UTF-8 byte constants for each keyboard keys
KEY_R = ord('r')
KEY_Q = ord('q')
VIDEO_DURATION_SECONDS = 15

# Opens a capture video from a default video capture device
#
# 0 = open default camera/device
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("[x] Failed to load video capture device")
    sys.exit(1)

# We need to get the capture device's width, height and its FPS for video encoding soon.
cap_frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_frame_fps = int(capture.get(cv2.CAP_PROP_FPS))

# Loads the XVID codec
xvid_codec = cv2.VideoWriter.fourcc(*"XVID")

# Getting how many frames we need to have it in 15 seconds
required_frames = cap_frame_fps * VIDEO_DURATION_SECONDS

# Writer file stream for the recorded video
writer: cv2.VideoWriter = cv2.VideoWriter(
    filename="output.mp4",
    fourcc=xvid_codec,
    fps=cap_frame_fps,
    frameSize=(cap_frame_width, cap_frame_height)
)

# Main loop of the recorder
for _ in range(required_frames):
    ret, frame = capture.read()

    # If no frames are grabbed, there's something wrong with the
    # video capture card, so we need to close it immediately.
    if not ret: break

    cv2.imshow("Recording...", frame)
    writer.write(frame)

    # Press 'q' to close the webcam feed window
    last_pressed_key = cv2.waitKey(1) & 0xFF
    if last_pressed_key == KEY_Q:
        break

print("[/] Saved recorded video at output.mp4")

writer.release()
capture.release()
cv2.destroyAllWindows()
