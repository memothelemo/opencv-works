import cv2
import sys

# Opens a capture video from a default video capture device
#
# 0 = open default camera/device
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("[x] Failed to load video capture device")
    sys.exit(1)

# We need to get the capture device's width, height and its FPS
# for video encoding soon.
cap_frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_frame_fps = capture.get(cv2.CAP_PROP_FPS)

# Loads the AVC1 codec
avc1_codec = cv2.VideoWriter.fourcc(*"avc1")

# Writer file stream for the recorded video
out = cv2.VideoWriter(
    filename="output.mp4",
    fourcc=avc1_codec,
    fps=cap_frame_fps,
    frameSize=(cap_frame_width, cap_frame_height)
)

while True:
    ret, frame = capture.read()

    # If no frames are grabbed, there's something wrong with the
    # video capture card, so we need to close it immediately.
    if not ret: break

    out.write(frame)
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to close the webcam feed window and stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
