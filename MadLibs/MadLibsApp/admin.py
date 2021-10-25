from django.contrib import admin
from .models import MadLibsStorage, MadLibsUserInput

# Register your models here.


admin.site.register(MadLibsStorage)
admin.site.register(MadLibsUserInput)
