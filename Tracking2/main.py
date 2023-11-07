import math
import time
import cv2
import pyautogui

R = 6373.0

def init_tracker(tracker_type):
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()

        # Define an initial bounding box
        init_bbox = (620, 236, 100, 100)
        # frame = cv2.imread("images/map.jpg")
        # Uncomment the line below to select a different bounding box
        #init_bbox = cv2.selectROI(frame, False)

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, init_bbox)
        return ok, tracker, init_bbox

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]

    pyautogui.screenshot("straight_to_disk.png", region=(341, 136, 1336, 583))
    frame = cv2.imread("straight_to_disk.png")
    ok, tracker, init_bbox = init_tracker(tracker_type)
    bbox = init_bbox
    init_x = 670
    init_y = 288
    # Get initial coordinate
    f = open("center_tracking.txt","r")
    inf = f.readline()
    lst = list(map(float, inf.split()))
    inital_lon = lst[0]
    inital_lat = lst[1]
    exactly_lon = inital_lon
    exactly_lat = inital_lat
    scale = lst[2]
    f.close()
    r_earth = 6378000
    pi = 3.1415

    cur_lat = inital_lat
    cur_lon = inital_lon
    cur_x = init_x
    cur_y = init_y

    while True:
        #get GPS coordinates
        f = open("center_tracking.txt", "r")
        inf = f.readline()
        lst = list(map(float, inf.split()))
        if len(lst):
            exactly_lon = lst[0]
            exactly_lat = lst[1]
            scale = lst[2]
        f.close()

        pyautogui.screenshot("straight_to_disk.png",region=(341,136, 1336, 583))
        frame = cv2.imread("straight_to_disk.png")

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # Draw bounding box
        if ok and int(bbox[0] + bbox[2] / 2) < 1000 and int(bbox[0] + bbox[2] / 2) > 300 and int(bbox[1] + bbox[3] / 2) > 150 and int(bbox[1] + bbox[3] / 2) < 400:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cur_x = int(bbox[0] + bbox[2] / 2)
            cur_y = int(bbox[1] + bbox[3] / 2)
            d_x = init_x - cur_x
            d_y = init_y - cur_y
            dist_x = d_x * 0.0002645833 * scale
            dist_y = d_y * 0.0002645833 * scale
            cur_lon = inital_lon - (dist_y / r_earth) * (180 / pi)
            cur_lat = inital_lat + (dist_x / r_earth) * (180 / pi) / math.cos(cur_lon * pi / 180)
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cur_x = init_x
            cur_y = init_y
            inital_lat = cur_lat
            inital_lon = cur_lon

            # cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            ok, tracker, init_bbox = init_tracker(tracker_type)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display coordinate on frame
        cv2.putText(frame, str(cur_lon) + " " + str(cur_lat), (500, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        dlat = exactly_lon - cur_lon
        dlon = exactly_lat - cur_lat
        a = (math.sin(dlat / 2)) ** 2 + math.cos(exactly_lat) * math.cos(cur_lat) * (math.sin(dlon / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        print(cur_lon, cur_lat, " ", exactly_lon, exactly_lat, " ", distance)
        # Display result
        cv2.imshow("Tracking", frame)
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break

