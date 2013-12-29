import cv2
import time
from managers import *
import datetime
from jsonEncoder import  Transit_Report
import simplejson
import logging

class Main(object):
	def __init__(self, w_name, source, mirrored=True):

		#Window manager takes 2 arguments <the window name>, <and some event to procces>
		self._windowManager = WindowManager(w_name, self.onKeypress)
		logging.basicConfig(level=logging.DEBUG)
		# captureManager takes 2 arguments <The video source or image source> , the windowManager
		self._captureManager= CaptureManager(cv2.VideoCapture("video.mp4"), self._windowManager)
		self.url_post = "http://127.0.0.1:8080/traffic_report/json"
		self.url_get = "http://127.0.0.1:8080/traffic_report/get_json"		
		self.tr = Transit_Report(2,1) # Id for cars_passed and for cameraset
		self.tr.from_now() # Count time from now

	def run(self):
		"""Run the main loop"""
		self._windowManager.createWindow()
		while self._windowManager.isWindowCreated:
			# Let one frame enter
			self._captureManager.enterFrame()
			# Grab the frame entered and show it
			self._captureManager.getFrame()
			# Procces keyboard events (Window managment)
			self._windowManager.processEvents()
			time.sleep(0.1)

	# Keyboard callback
	def onKeypress(self, keycode):
		"""
		Handle a onKeypress

		escape	-> Quit.
		"""
		if keycode == 27: #escape
			self._windowManager.destroyWindow()
			#self.send_json()
		

	def counter():
		pass
	def send_json(self):
		try:
			respons = urllib2.urlopen(self.url_get)
			data = simplejson.load(respons)
			print self._captureManager.get_count()
			self.tr.cars_passed_id = data['ID']+1 # ID + 1
			self.tr.set_cars(self._captureManager.get_count(), 0, self._captureManager.get_count(),datetime.datetime.now().isoformat() )
		# 1er parametro carros que pasaron
		# 2do .parametro carros parados
		# 3er param cantidad de carros
		# 4to param fecha y hora de finalizacion
			self.tr.Gen() # genera el json
			self.tr.POST(self.url_post) #postea el json
#			tr.set_cars()
			print  "Saved with ID: "+str(data['ID']+1)
	#		tr.POST(self.url)
		except Exception, ex:
			logging.debug("Inside send_json or the server..!")
			logging.exception("Error it cannot sync")



			

if __name__ == "__main__":
	Main = Main("Main", 0)
	Main.run()
