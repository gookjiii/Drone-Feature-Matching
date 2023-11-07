import np as np
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# import FOVDetect as fov

img1 = cv.imread('images/test.png', cv.IMREAD_GRAYSCALE) # queryImage
img2 = cv.imread('images/train.png', cv.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detectorv
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
# while True:
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

while True:
    # Apply ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.30*n.distance:
            good_matches.append(m)

# Sort them in the order of their distance.

    good_matches = sorted(good_matches, key=lambda x: x.distance)
    if len(good_matches)>10:
        try:
            good_matches = good_matches[:50]
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            h,w = img1.shape[:2]
            pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
            # pts = np.float32([fov.IntersetA[:2], fov.IntersetB[:2], fov.IntersetC[:2], fov.IntersetD[:2]]).reshape(-1,1,2)
            dst = cv.perspectiveTransform(pts, M)
            # dst += (0, 0)
            dst += (w, 0)  # adding offset
            draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                           singlePointColor = None,
                           matchesMask = matchesMask, # draw only inliersc
                           flags = 2)

            img3 = cv.drawMatches(img1,kp1,img2,kp2,good_matches, None,**draw_params)

            # Draw bounding box in Red
            img3 = cv.polylines(img3, [np.int32(dst)], True, (0,0,255),3, cv.LINE_AA)
        except:
            img3 = img2
    else:
        img3 = img2

    cv.imshow("result", img3)
    # cv.resizeWindow("result",1600,900)
    if cv.waitKey(1) & 0xFF == ord('c'):  # save on pressing 'c'
        cv.destroyAllWindows()
        break