import cv2
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# check if webcam is opened

if not cap.isOpened():
    cap = cv2.VideoCapture(1)
if not cap.isOpened:
    raise IOError("Cannot open webcam")
emotion = []
while True:
    ret, frame = cap.read()  # read one image from video
    result = DeepFace.analyze(frame, actions=['emotion'])
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(faceCascade.empty())
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    if result['dominant_emotion'] == 'happy':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (208, 224, 64), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (208, 224, 64),
                    2,
                    cv2.LINE_4)
    if result['dominant_emotion'] == 'neutral':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (255, 255, 255),
                    2,
                    cv2.LINE_4)
    if result['dominant_emotion'] == 'angry':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (0, 0, 255),
                    2,
                    cv2.LINE_4)
    if result['dominant_emotion'] == 'sad':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (255, 0, 0),
                    2,
                    cv2.LINE_4)
    if result['dominant_emotion'] == 'fear':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (0, 255, 0),
                    2,
                    cv2.LINE_4)
    if result['dominant_emotion'] == 'surprise':
        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (50, 50),
                    font, 3,
                    (255, 0, 255),
                    2,
                    cv2.LINE_4)
    # notFull = True
    # while True and len(emotion) <= 1:
    #     if notFull:
    #         if len(emotion) <= 1:
    #             emotion.append(result['dominant_emotion'])
    #             print(emotion[0])
    #             notFull = False
    #     break

    cv2.imshow('Original Video', frame)

    if cv2.waitKey(2) % 0xff == ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
