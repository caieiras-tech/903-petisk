from django.contrib import admin
from website.models import Pessoa, Ong, Pet

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Ong)
admin.site.register(Pet)