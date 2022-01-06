from django.contrib import admin
from .models import Education, FirstSection , About_Basic_Information ,Skills , Projects , Experience 

# Register your models here.
admin.site.register(FirstSection)
admin.site.register(About_Basic_Information)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(Experience)
admin.site.register(Education)

