import cv2
import pafy

url ="https://www.youtube.com/watch?v=z_fY1pj1VBw"
video = pafy.new(url)
stream = video.getbest(preftype="mp4")
cap = cv2.VideoCapture(stream.url)

while True:
    success, image = cap.read()
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    if success:
        cv2.imshow("image", image)

    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()


