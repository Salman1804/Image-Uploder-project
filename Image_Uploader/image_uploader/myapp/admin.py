from django.contrib import admin
from myapp.models import image

# Register your models here.
@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    list_display=['id','title','image']