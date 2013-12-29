# Create your views here.
from views import *
from traffic_report.models import cars_passed, camera_set
from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core import serializers
import django.utils.simplejson as json
from django.utils import simplejson
import sys, datetime,json,ast
from django.views.decorators.csrf import csrf_exempt


# import the logging library
#import logging

# Get an instance of a logger
#logger = logging.getLogger(__name__)

@csrf_exempt
def get_json(request):
	try:
		car = cars_passed.objects.latest('ID')
	except:
		print >>sys.stderr, "No cars registered, creating it...."
		st_date = datetime.datetime.now()
		nd_date = datetime.datetime.now()

		cars = cars_passed(ID=0, cars_passed=0, cars_jammed=0, cars_quantity=0, start_date=st_date, end_date=nd_date)
		cars.save()
		car = cars_passed.objects.latest('ID')
	lis = 	{
		"ID" : car.ID,
		"cars_passed" :car.cars_passed,
		"cars_jammed": car.cars_jammed,
		"cars_quantity": car.cars_quantity,
		"start_data": car.start_date.strftime("%Y-%m-%d %H:%M:%S"),
		"end_date": car.end_date.strftime("%Y-%m-%d %H:%M:%S"),
	          }
	return HttpResponse(simplejson.dumps(lis) , mimetype='application/json')


#def json(request):
#	if not request.is_ajax():
#		raise Http404
#	data = 
@csrf_exempt

def json(request):
#	if request.is_ajax():
	print >>sys.stderr,'this!'
#	if request.method == 'POST':
	json_data = simplejson.loads(request.raw_post_data)
	print >> sys.stderr, type(request.raw_post_data)
	print >>sys.stderr, type(json_data)
#	json_data = simplejson.dumps(json_data)
	print >>sys.stderr, type(json_data)
	try:
		print >>sys.stderr, "json baby"			
#		print >>sys.stderr, json_data.get("ID")
	#	liss = json_data.values()
	#	lisst = list(liss)
#	for j in json_data:
		j = ast.literal_eval(json_data)
		print >>sys.stderr, type(j)
		print >>sys.stderr, type(json_data)
		car_id = j['ID']
		cars_pass = j['cars_passed'] 
		cars_jamm = j['cars_jammed']
		cars_quant = j['cars_quantity']
				#		cars_quant = liss[4]
		st_date = j['start_date']	
#		st_date = liss[2]
		nd_date = j['end_date']
#		nd_date = liss[1]
		cars = cars_passed(ID=car_id, cars_passed=cars_pass, cars_jammed=cars_jamm, cars_quantity=cars_quant, start_date=st_date, end_date=nd_date)
		cars.save()
	except KeyError:
		HttpResponseServerError("Malformed Data")
		HttpResponse("Got Json")

#			with open('./this.json', 'w') as out:
#				JSONSerializer = serializers.get_serializer("json")
#				json_serializer = JSONSerializer()	
#				json_serializer.serialize(request.raw_post_data, stream=out)
	return HttpResponse('Raw Data: "%s"' % request.raw_post_data)
	print 'done'

#			print 'Raw Data: "%s"'% request.raw_post_data
	print >>sys.stderr, "hola"
	return HttpResponse("cool")


def index(request):
	"""
	lastest_camera_list = camera_set.objects.all().order_by('-status')[:5]
	return render_to_response('traffic_report/index.html',{'lastest_camera_list' : lastest_camera_list} )

"""

#	lastest_cars_list = cars_passed.objects.all().order_by('-start_date')[:5]
#	output = ', '.join([ str(p.cars_passed) for p in lastest_cars_list])
#	return HttpResponse(output)
#	lastest_cars_list = cars_passed.objects.all().order_by('-start_date')[:5]
#	t = loader.get_template('traffic_report/index.html')
#	c = Context({'lastest_cars_list' : lastest_cars_list,})
#	return HttpResponse(t.render(c))

# Render to response method
	lastest_cars_list = cars_passed.objects.all().order_by('-start_date')[:5]
	JSONSerializer = serializers.get_serializer("json")
	json_serializer = JSONSerializer()
	with open("./file.json", "w") as out:
		json_serializer.serialize(cars_passed.objects.all(), stream=out)
	return render_to_response('traffic_report/index.html',{'lastest_cars_list' : lastest_cars_list} )



def results(request, cars_passed_id):
	return HttpResponse("You're looking at the results of cars_passed %s." % cars_passed_id)

def vote(request, cars_passed_id):
	return HttpResponse("You're voting on cars_passed %s." % cars_passed_id)

"""

def results(request, camera_set_id):
	return HttpResponse("You're looking at the results of cars_passed %s." % camera_set_id)

def vote(request, camera_set_id):
	return HttpResponse("You're voting on cars_passed %s." % camera_set_id)

"""
def viewer(request):
	return render_to_response('traffic_report/index.html')

def detail(request, cars_passed_id):
	try:
		cars = cars_passed.objects.get(pk=cars_passed_id)
	except cars_passed.DoesNotExist:
		raise Http404
	return render_to_response('traffic_report/detail.html', {'cars_passed': cars })
