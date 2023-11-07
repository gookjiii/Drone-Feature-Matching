import cv2
import sys


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
        if tracker_type == 'CSRT':
            tracker = cv2.TrackerCSRT_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()

        # Define an initial bounding box
        init_bbox = (1200, 500, 100, 100)
        # frame = cv2.imread("images/map.jpg")
        # Uncomment the line below to select a different bounding box
        #init_bbox = cv2.selectROI(frame, False)

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, init_bbox)
        return ok, tracker, init_bbox

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE','GOTURN']
    tracker_type = tracker_types[2]


    # Read video
    video = cv2.VideoCapture("./mixkit-aerial-view-of-a-river-with-people-in-and-around-43615")
    # video = cv2.VideoCapture(0)

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()

    ok, tracker, init_bbox = init_tracker(tracker_type)
    bbox = init_bbox

    while True:
        #print(init_bbox)
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok and int(bbox[0] + bbox[2] / 2) < 1900 and int(bbox[0] + bbox[2] / 2) > 300 and int(bbox[1] + bbox[3] / 2) > 300 and int(bbox[1] + bbox[3] / 2) < 800:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            ok, tracker, init_bbox = init_tracker(tracker_type)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("Tracking", frame)
        
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break