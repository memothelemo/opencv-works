import cv2
import sys

from time import time

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

# Writer file stream for the recorded video
writer: cv2.VideoWriter | None = None

# Last timestamp of when this program started recording
started_recording_at = None

# Main loop of the recorder
while True:
    ret, frame = capture.read()

    # If no frames are grabbed, there's something wrong with the
    # video capture card, so we need to close it immediately.
    if not ret: break

    cv2.imshow("Webcam Feed", frame)

    # Recording stream stuff
    if started_recording_at is not None:
        assert writer is not None
        writer.write(frame)

        current_timestamp = int(time())
        elapsed = current_timestamp - started_recording_at
        if elapsed > VIDEO_DURATION_SECONDS:
            print("[/] Video recording stopped.")
            writer.release()
            writer = None
            started_recording_at = None

    # Capture any pressed keys from the keyboard
    last_pressed_key = cv2.waitKey(1) & 0xFF
    if last_pressed_key == KEY_Q:
        # Press 'q' to close the webcam feed window
        break
    elif last_pressed_key == KEY_R and started_recording_at is None:
        # Press 'r' to record a video from video capture frames for 15 seconds
        started_recording_at = int(time())
        writer = cv2.VideoWriter(
            filename="output.mp4",
            fourcc=xvid_codec,
            fps=cap_frame_fps,
            frameSize=(cap_frame_width, cap_frame_height)
        )
        print(f"[!] Recording video from webcam for {VIDEO_DURATION_SECONDS} second(s)")

# If the program is about to exit while it is recording, we can stop from there.
if writer is not None:
    writer.release()

capture.release()
cv2.destroyAllWindows()
