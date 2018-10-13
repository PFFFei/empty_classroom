from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(Saturday)
admin.site.register(Sunday)

#admin.site.register([Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday])
