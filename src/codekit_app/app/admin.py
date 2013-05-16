
from django.contrib import admin

from app.models import Task, Check, Block, Language
 
admin.site.register(Task)
admin.site.register(Check) 
admin.site.register(Block)
admin.site.register(Language)

