from django.contrib import admin

# Register your models here.
from .models import Emp,Testimonial



class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','emp_id')
    search_fields=('name','phone')
    list_filter=('working',)

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)