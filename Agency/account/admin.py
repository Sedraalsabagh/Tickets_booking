from django.contrib import admin
from . models import User, Customer,UserProfile #,Employee 

# Register your models here.


admin.site.register(User)
admin.site.register(Customer)
#admin.site.register(Employee)

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','date_of_birth','photo']
    raw_id_fields=['user']
   