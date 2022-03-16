import cv2
image1 = cv2.imread('photo01.jpg')
image2 = cv2.imread('photo02.jpg')
h, w, c = image1.shape
image1 = cv2.resize(image1, (int(w/5),int(h/5)))
image2 = cv2.resize(image2, (int(w/5),int(h/5)))

def nothing(X): pass

cv2.namedWindow('TrackBar')
cv2.createTrackbar('%','TrackBar', 0, 100, nothing)
while True:
    r = cv2.getTrackbarPos('%','TrackBar')
    r = float(r)*0.01
    imageAddwe = cv2.addWeighted(image2, r, image1, 1-r, 0)
    cv2.imshow('TrackBar',imageAddwe)
    if cv2.waitKey(1) & 0xFF == 27: break

cv2.destroyWindow('TrackBar')