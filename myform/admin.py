from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Form)
admin.site.register(TextForm)
admin.site.register(TextAnswer)
admin.site.register(McqForm)
admin.site.register(McqAnswer)
admin.site.register(BoolForm)
admin.site.register(BoolAnswer)
admin.site.register(TestInput)