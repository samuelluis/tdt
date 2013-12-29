from collections import Mapping, Sequence
from unittest import TestCase, main
import io, json
import requests
#rom django.test.client import Client
#rom django.test.utils import setup_test_enviroment
import urllib2


# ***********************************************************

# Transit Report 0.5
# Written by: Aqt01
# Used to send the reported status of a transit camera

""""
 Ecclesiastes 18 For with much wisdom comes much sorrow;
    the more knowledge, the more grief.

    Isaiah. 55.6 Seek the Lord while he may be found;
    call on him while he is near.

    John 8.32 And you will know the truth, and the 
    truth will make you free.
"""
# ***********************************************************





class Transit_Report:
  
    def __init__(self, cars_passed_id,cameraset_id):
      self.cars_passed_id = cars_passed_id
      self.cameraset_id = cameraset_id

    def set_cars(self, cars_passed, cars_jammed,cars_quantity, start_date, end_date ):
      self.cars_passed = cars_passed
      self.cars_jammed = cars_jammed
      self.cars_quantity = cars_quantity
      self.start_date = start_date
      self.end_date = end_date

    def set_camera(self, camera_id,camera_status):
      self.camera_id = camera_id
      self.camera_status = camera_status
      

            #untrusted = json.dumps(round_floats(val),outfile)
    def Gen(self): #This is for generating the json.. as just the def function says..
	    self.payload = json.dumps( { 'ID' : self.cars_passed_id ,'cars_passed': self.cars_passed,'cars_jammed': self.cars_jammed, 'cars_quantity' : self.cars_quantity, 'start_date': self.start_date , 'end_date': self.end_date, } ) 
#        , 'cameraset_id':self.cameraset_id , 'cameraset_updated': [{ 'id': self.cameraset_id_updated , 'status': self.camera_status }] })
      
    def print_json(self):
      self.Gen()
      print self.payload

    def POST(self, url):
      self.Gen()
      self.url = url
#      urllib2.urlopen(self.url, urllib.urlencode(self.payload) )
      req = urllib2.Request(self.url)
      req.add_header('Content-Type', 'application/json')
      response = urllib2.urlopen(req,json.dumps(self.payload))
   #   r = requests.post(url, data=self.payload)
      print response #Testing purposes, this prints the status of the post response of http://httpbin.org/post
      #print r.text



class OCR:
  
    def __init__(self, ID):
      self.ID = ID
     
    def set_OCR(self, matricula, fecha, hora , img_url):
      self.matricula = matricula
      self.fecha = fecha
      self.hora = hora
      self.img_url = img_url

    def set_camera(self, camera_id,camera_status):
      self.camera_id = camera_id
      self.camera_status = camera_status
      

    def Gen(self): #This is for generating the json.. as just the def function says..
	    self.payload = json.dumps( {"registration_tags": [ { 'ID' : self.ID ,'matricula': self.matricula,'date': self.fecha, 'hour' : self.hora, 'img_url' : self.img_url  } ] } ) 
#        , 'cameraset_id':self.cameraset_id , 'cameraset_updated': [{ 'id': self.cameraset_id_updated , 'status': self.camera_status }] })
      
    def print_json(self):
      self.Gen()
      print self.payload

    def save_file(self,path):
      with open(path+"ocr.json", "w") as text_file:
      	text_file.write( str(self.payload) )
     	text_file.close()

    def POST(self, url):
      self.Gen()
      self.url = url
#      urllib2.urlopen(self.url, urllib.urlencode(self.payload) )
      req = urllib2.Request(self.url)
      req.add_header('Content-Type', 'application/json')
      response = urllib2.urlopen(req,json.dumps(self.payload))
   #   r = requests.post(url, data=self.payload)
      print response #Testing purposes, this prints the status of the post response of http://httpbin.org/post
      #print r.text


def main(): 
 # Example with transit report
  hey = Transit_Report(50,2)
  #hey.set_camera(2,'no',1)
  hey.set_cars(2,2,4,'2013-4-13','2013-4-13')
  hey.print_json()
#  hey.POST("http://127.0.0.1:8080/traffic_report/json")
 # Example with OCR
  ho = OCR(1)
  ho.set_OCR(1,"12-12-12","13:00","pollo.jpg")
  ho.Gen()
  ho.save_file("./")
  ho.print_json()
# ho.POST("127.0.0.1/viewer/view")


if __name__ == '__main__':
    main()
