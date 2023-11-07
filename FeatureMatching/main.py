import cv2
import numpy as np
import matplotlib.pyplot as plt

#img1 = cv2.imread('Screenshot 2022-09-11 221006.jpg', 0)
img2 = cv2.imread('images/WIN_20220913_16_58_12_Pro.jpg', 0)

sift = cv2.SIFT_create()

cap = cv2.VideoCapture(0)

kp2, des2 = sift.detectAndCompute(img2, None)

while True:
    ret, img1 = cap.read()
    kp1, des1 = sift.detectAndCompute(img1, None)
    FLANN_INDEX_kdTREE = 1
    index_params = dict(algorithm = 1, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2, k = 2)

    matchesMask = [[0,0] for i in range(len(matches))]

    for i,(m,n) in enumerate(matches):
        if m.distance < 0.4*n.distance:
            matchesMask[i] = [1,0]

    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor= (255,0,0),
                       matchesMask = matchesMask,
                       flags = cv2.DrawMatchesFlags_DEFAULT)
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    plt.imshow(img3)
    plt.show()