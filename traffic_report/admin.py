from django.contrib import admin
from traffic_report.models import cars_passed, camera_set

#admin.site.register(cars_passed)

#admin.site.register(camera_set)

#class cars_passedInline(admin.StackedInline):
#	model = cars_passed
#	extra = 0

class camera_setInline(admin.StackedInline):
	model = camera_set
	extra = 0


class cars_passedAdmin(admin.ModelAdmin):
	#fields = ['cars_passed', 'cars_quantity']
	fieldsets=[('Start Date', {'fields': ['start_date']}), ('information', {'fields': ['ID','cars_passed', 'cars_jammed','cars_quantity'], 'classes': ['collapse'] } ), ('End Date',{'fields': ['end_date'], 'classes':['collapse']}), ]
	inlines = [camera_setInline]
	list_display = ('ID','cars_passed', 'cars_jammed','cars_quantity','start_date', 'end_date')
	search_fields = ['start_date']
	date_hierarchy = 'start_date'

"""
class camera_setAdmin(admin.ModelAdmin):
#fields = ['cars_passed', 'cars_quantity']
	fieldsets=[('Start Date', {'fields': ['cars_passed__start_date']}), ('information', {'fields': ['cars_passed__ID','cars_passed__cars_passed', 'cars_passed__cars_jammed','cars_passed__cars_quantity'], 'classes': ['collapse'] } ), ('End Date',{'fields': ['cars_passed__end_date'], 'classes':['collapse']}), ]
	inlines = [cars_passedInline]
	list_display = ('cars_passed__ID','cars_passed__cars_passed', 'cars_passed__cars_jammed','cars__passed__cars_quantity','cars_passed__start_date', 'cars_passed__end_date')
	search_fields = ['cars_passed__start_date']
	date_hierarchy = 'cars_passed__start_date'


"""
admin.site.register(cars_passed,cars_passedAdmin)


#class cars_passedInline(admin.StackedInline):
#	model = cars_passed
#	extra = 2
"""
class camera_setAdmin(admin.ModelAdmin):
	#fields = ['cars_passed', 'cars_quantity']
	fieldsets=[('Camera ', {'fields': ['camera_id']}), ('Status', {'fields': ['status'], 'classes': ['collapse'] } ),]
	inlines = [cars_passedInline]
	list_display = ('camera_id', 'status')
	search_fields = ['camera_id']
	date_hierarchy = 'camera_id'
#	date_hierarchy = 'start_date'

"""

#admin.site.register(camera_set,camera_setAdmin)

