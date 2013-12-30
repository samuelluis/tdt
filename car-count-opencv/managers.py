import cv2
import cv
import time
import numpy
import numpy as np
#import base64
#import urllib2


class CaptureManager(object):
	def __init__(self, capture, previewWindowManager = None):
		self.previewWindowManager = previewWindowManager
		self._capture = capture
		self._channel = 0
		self._enteredFrame = False
		self._frame = None
		self._state = 0
		self._counter = 0

		# 3 Image variables (Used in detectMotion method)
		self._image0 = None
		self._image1 = None
		self._image2 = None

		# List, will be use to store motion in frames
		self._list = []
		self._list1 = []

		# State variables
		self._drawing = False
		self._mode = True
		self._ix = -1
		self._iy = -1
		self._startCounter = False

		# Roi draw points
		self._roiy = 0
		self._roix = 0
		self._roiyy= 0
		self._roixx = 0

		# List container of mouseEvents
		self._eventList = []

		#List container of threshold values
		self._threshold = []
		self._dimg = None



	@property
	def channel(self):
		return self._channel

	@channel.setter
	def channel(self, value):
		if self._channel != value:
			self._channel = value
			self._frame = None

	@property
	def frame(self):
		"""Returns a frame of the captured image"""
		if self._enteredFrame and self._frame is None:
				_, self._frame = self._capture.retrieve(channel = self._channel)
		return self._frame

	def getFrame(self):
		"""Gets a frame and show it"""
		#Is there is no frame , set entered frame to False.
		if self.frame is None:
			self._enteredFrame = False
			return

		# Draw to the window, if any
		if self.previewWindowManager is not None:
			self.detectMotion()
			if self._dimg != None:
				self.previewWindowManager.show(self._dimg) #self._frame



		#Sets frame to None, to get the other frame of the capture
		self._frame = None
		self._enteredFrame = False

	def enterFrame(self):
		"""Capture the next frame, if any """
		# But first, check that any previous frame was exited
		if self._capture is not None:
			self._enteredFrame = self._capture.grab()

	def detectMotion(self):
		"""Detect motion using absolute difference, and returns the motion in a roi section"""

		#Using a state variable will make sure that this section only runs once, like setup
		if self._state == 0:
			self._image0 = cv2.cvtColor(self._frame, cv2.COLOR_RGB2GRAY)
			self._image1 = cv2.cvtColor(self._frame, cv2.COLOR_RGB2GRAY)
			self._image2 = cv2.cvtColor(self._frame, cv2.COLOR_RGB2GRAY)
			#height, width =  self._image0.shape
			#self.previewWindowManager.video.open('/home/samuel/video.avi',cv2.cv.CV_FOURCC('D', 'I', 'V', 'X'),4.0,(width,height))
			#print(self.previewWindowManager.video.isOpened())

		# Setting this variable to 1 makes that the above section only runs once.
		self._state = 1

		self._image0 = self._image1
		self._image1 = self._image2
		self._image2 = cv2.cvtColor(self._frame, cv2.COLOR_RGB2GRAY)

		# Gets the difference between 3 images.
		self._dimg = self.diffImg(self._image0, self._image1, self._image2)

		# CountNonZero returns how much has the images change in relation to each other (Motion).
		motion = cv2.countNonZero(self._dimg)


		return motion

	def counter(self):
		pass

	def get_count(self):
		return self._counter


	def diffImg(self, t0, t1, t2):
		"""Uses absdiff to determine the difference between 2 images"""
		# Gets the difference between 2 images
		d1 = cv2.absdiff(t2, t1)
		d2 = cv2.absdiff(t1, t0)
		# Returns the bitwise_and between d1 and d2
  		return cv2.bitwise_and(d1, d2)

 

class WindowManager(object):
	def __init__(self, windowName, keypressCallback = None):
		self.keypressCallback = keypressCallback
		self._count = 0
		self._windowName = windowName
		self._isWindowCreated = False
		#self.video = cv2.VideoWriter()

	@property 
	def isWindowCreated(self):
		return self._isWindowCreated

	def createWindow(self):
		cv2.namedWindow(self._windowName)
		self._isWindowCreated = True

	def show(self, frame):
		#cv2.line(frame, (190,500), (550,450), (255,0,0), 2)
		#cv2.line(frame, (810,420), (1160,360), (255,0,0), 2)
		cv2.imshow(self._windowName, frame)
		#cv2.imwrite("imgs/img"+(`self._count`)+".png", frame)
		print("imgs/img"+(`self._count`)+".png")
		self._count+=1
		#self.video.write(frame)
		#print("write frame")


	def destroyWindow(self):
		cv2.destroyWindow(self._windowName)
		self._isWindowCreated = False
		#self.video.release()
		#print("video release")

	def getWname(self):
		return self._windowName


	def processEvents(self):
		keycode = cv2.waitKey(1)
		if self.keypressCallback is not None and keycode != -1:
			#Discard any non-Ascii info encoded by GTK.
			keycode &= 0xFF
			self.keypressCallback(keycode)
