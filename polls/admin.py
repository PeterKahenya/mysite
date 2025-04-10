from django.contrib import admin

from polls.models import Choice, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
