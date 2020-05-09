import dlib
import cv2
import sys
from imutils import face_utils
import numpy as np

SCALE_FACTOR = 0.2


def featureDetection(image):
    detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')
    predictor = dlib.shape_predictor('landmarkDetector.dat')
    img = cv2.imread(f"./static/images/{image}")
    img_result = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, dsize=None, fx=SCALE_FACTOR, fy=SCALE_FACTOR)

    dets = detector(img, upsample_num_times=1)

    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))
        x1, y1 = int(d.rect.left() /
                     SCALE_FACTOR), int(d.rect.top() / SCALE_FACTOR)
        x2, y2 = int(d.rect.right() /
                     SCALE_FACTOR), int(d.rect.bottom() / SCALE_FACTOR)

        cv2.rectangle(img_result, pt1=(x1, y1), pt2=(x2, y2),
                      thickness=2, color=(255, 0, 0), lineType=cv2.LINE_AA)

        shape = predictor(img, d.rect)
        shape = face_utils.shape_to_np(shape)

        for i, p in enumerate(shape):
            cv2.circle(img_result, center=tuple((p / SCALE_FACTOR).astype(int)),
                       radius=5, color=(0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)
            cv2.putText(img_result, str(i), tuple((p / SCALE_FACTOR).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imwrite(f"./static/images/f{image}", img_result)
