from django.contrib import admin
from .models import Account,Room,RoomMessage,RoomNotification
# Register your models here.



admin.site.register(Account)
admin.site.register(RoomMessage)
admin.site.register(Room)
admin.site.register(RoomNotification)