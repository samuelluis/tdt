#!/usr/bin/env python
import cv2.cv as cv
import cv2
import numpy as np
import tesseract
import time
import datetime
from jsonEncoder import  OCR
import simplejson
import logging
import urllib2

class ocr(object):
	def __init__(self, image=None):
		# Initializing the tesseract api.
		self.api = tesseract.TessBaseAPI()
		self.api.Init(".", "eng", tesseract.OEM_DEFAULT)

		# Needed namespaces
		self.text = ""
		self.image = image
		self.path = ""
		
	def load_image(self, image):
		"""Loads image with opencv"""
		self._image = image
		self.image = cv.LoadImage(self._image)

	def gen_text(self):
		"""Generates the text on the image"""
		tesseract.SetCvImage(self.image, self.api)
		self.text=self.api.GetUTF8Text()
		self.conf=self.api.MeanTextConf()
		self.url = "http://httpbin.org/post" # <.< url de prueba, debe ser modificado
		self.send_json(self.text,self.url)

	def get_text(self):
		"""Retrieve the text taken from the image."""
		return self.text


	def send_json(self, text,url): # TO send json, text sera la matricula
		self.url_get = url # URL to send json, this one is for testing
		try:
			#respons = urllib2.urlopen(self.url_get)
			#data = simplejson.load(respons)
			#print self._captureManager.get_count()
			#self.tr.cars_passed_id = data['ID']+1 # ID + 1
			self.OCR = OCR(1) # OCR con ID FIJO
			
			#Change to your path
			self.path = self._image.replace("/home/javier/Desktop/transitdatateam-tdt-6a65abdae81f/traffic_report/", "/")
			self.OCR.set_OCR(text,datetime.datetime.now().date().isoformat(), datetime.datetime.now().time().isoformat(), self.image) #texto, fecha y tiempo
			# 1er parametro carros que pasaron
			# 2do .parametro carros parados	
			# 3er param cantidad de carros
			# 4to param fecha y hora de finalizacion
			self.OCR.Gen() # genera el json
			self.OCR.print_json()
			#self.OCR.POST(self.url_get) #postea el json a la direccion que se le debe especificar
			self.OCR.save_file("/home/javier/Desktop/transitdatateam-tdt-6a65abdae81f/traffic_report/static/json/") #Graba el archivo en el path puestp
			print  "Saved with ID: "+str(self.OCR.ID)
	
		except Exception, ex:
			logging.debug("Inside send_json or the server..!")
			logging.exception("Error it cannot sync")

	def main(self):
		self.load_image(self.image)
		self.gen_text()
		text = self.get_text()
		print text

#Uncomment the lines below to use ocr object
if __name__ == "__main__":
	# Change to your path
	Ocr = ocr("/home/javier/Desktop/transitdatateam-tdt-6a65abdae81f/traffic_report/static/ocr_images/image3.jpg")	
	Ocr.main()
