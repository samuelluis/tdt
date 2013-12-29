from django.db import models
import datetime
from django.contrib import admin


class cars_passed(models.Model):
	
	#cameraset_id = models.IntegerField("cameraset_id",default=0)
	ID = models.IntegerField(primary_key=True)

	#camera_set = models.ForeignKey(camera_set)

	cars_passed = models.IntegerField('cars_passed')
	cars_jammed = models.IntegerField('cars_jammed')
	cars_quantity = models.IntegerField('cars_quantity')

	start_date = models.DateTimeField('start_date')
	end_date = models.DateTimeField('end_date')

	def __unicode__(self):
		ID_txt = "ID: " + str(self.ID)
		cars_passed_txt = "Cars passed: " + str(self.cars_passed)
		cars_jammed_txt = "Cars jammed: " + str (self.cars_jammed)
		cars_quantity_txt = "Cars quantity: " + str(self.cars_quantity)
		lst = []
		lst.append(self.start_date)
		lst.append(self.end_date)

		start_date_txt = "Start date: "# + str(lst[0])
		end_date_txt = "End date: " #+ str(lst[1])
		text = ID_txt + "\n" + cars_passed_txt + "\n" + cars_jammed_txt + "\n" + cars_quantity_txt + "\n" + start_date_txt + "\n" + end_date_txt + "\n"		
		return text



# Create your models here.

class camera_set(models.Model):
	ID = models.IntegerField(primary_key= True,default=0)
	cars_passed = models.ForeignKey(cars_passed, related_name='Cars passed ID')
	
	camera_id = models.IntegerField('camera_id')
	status = models.CharField(max_length=50)

	def __unicode(self):
#		camera_set_id_txt = "Camera set ID: " + int(self.id)
		ID_txt = "Cameraset ID: " + str(self.ID)
		camera_id_txt= "Camera ID: " + str(self.camera_id)
		status_txt = "Camera Status: " + self.status
		text =  ID_txt + "\n" + camera_id_txt + "\n" + status_txt + "\n"
		return text

