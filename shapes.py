#!/usr/bin/env python

import cv2

threshold_val = 127
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(grey, threshold_val, 255, cv2.THRESH_BINARY)
    im, contours, heirarchy = cv2.findContours(thresh,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)




    # use cv2.contourArea (0r moments) to rank by area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)  # broken
    n_cont = min(50, len(contours))
    #for c in contours[0:n_cont]:
    #    print(cv2.contourArea(c))
    #print('----')
    frame = cv2.drawContours(frame, contours[0:n_cont], -1, (0, 255, 0), 2)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('a'):
        threshold_val += 10
        print('threshold = {}'.format(threshold_val))
    elif key & 0xFF == ord('z'):
        threshold_val -= 10
        print('threshold = {}'.format(threshold_val))

cap.release()
cv2.destroyAllWindows()
