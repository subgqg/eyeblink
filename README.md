# eyeblink

This code uses the OpenCV library to detect faces and eyes in a video stream. The code begins by initializing two cascade classifiers, one for detecting faces and one for detecting eyes. These classifiers are trained using pre-existing XML files, 'haarcascade_frontalface_default.xml' and 'haarcascade_eye_face_eyeglasses.xml' respectively. The code then captures video from the default camera using the cv2.VideoCapture() function, and reads the first frame of the video.

The code then enters a while loop, where it continuously reads frames from the video stream and converts each frame to grayscale using cv2.cvtColor(). The grayscale image is then passed through a bilateral filter using cv2.bilateralFilter() to remove impurities. The filtered grayscale image is then passed through the face classifier using the detectMultiScale() method.

The detectMultiScale() method returns an array of rectangles representing the detected faces in the image. If there are any faces detected, the code then draws a rectangle around the detected face using the cv2.rectangle() function, with the top left corner at (x,y) and the bottom right corner at (x+w, y+h). The code will keep running this loop until there is no frames left in the video stream.
