import cv2
import cvzone  
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

# Web camera open
cap = cv2.VideoCapture(0)

# Face detector only 1 face
detector = FaceMeshDetector(maxFaces=1)

# Eye plot
plot = LivePlot(700, 400, [20, 50])

# FaceMesh eye landmarks
idList = [22, 23, 24, 26, 110, 130, 157, 159, 160, 161, 243]

blink_count = 0
blink_flag = 1   # start ready to detect blink

while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (800, 600))

    if not success:
        print("Frame not found")
        continue

    # Detect face
    frame, faces = detector.findFaceMesh(frame, draw=False)

    if faces:
        face = faces[0]

        # Draw eye landmarks
        for id in idList:
            cv2.circle(frame, face[id], 3, (255, 0, 255), cv2.FILLED)

        # Vertical eye distance
        leftUp = face[159]
        leftDown = face[23]
        Eye_VerLength, _ = detector.findDistance(leftUp, leftDown)
        cv2.line(frame, leftUp, leftDown, (0, 200, 0), 2)

        # Horizontal eye distance
        leftRight = face[130]
        leftLeft = face[243]
        Eye_HorLength, _ = detector.findDistance(leftRight, leftLeft)
        cv2.line(frame, leftRight, leftLeft, (0, 200, 0), 2)

        if Eye_HorLength != 0:
            ratio = (Eye_VerLength / Eye_HorLength) * 100
            print(ratio)

            # Blink detection
            if ratio < 38 and blink_flag == 1:
                blink_count += 1
                blink_flag = 0
            elif ratio > 33 and blink_flag == 0:
                blink_flag = 1

            # Display
            cvzone.putTextRect(
                frame,
                f'Blink Count: {blink_count}',
                (50, 80),
                scale=2,
                thickness=2,
                colorT=(255, 255, 255)
            )

            cv2.imshow("Plot", plot.update(ratio))

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
