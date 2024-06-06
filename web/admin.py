from django.contrib import admin
from web.models import Usuario, Inmueble, Region, Comuna, SolicitudArriendo
# Register your models here.
 
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(SolicitudArriendo)