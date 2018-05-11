from django.contrib import admin
from .models import Desk, DeskWorkers, DeskToDo, Article

admin.site.register(Desk)
admin.site.register(DeskWorkers)
admin.site.register(DeskToDo)
admin.site.register(Article)
