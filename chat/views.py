from django.shortcuts import render



from .models import Account,Room,RoomMessage,RoomNotification
# Create your views here.





def index(request):
    return render(request,'index.html')


def auth_(request):
    return render(request,'auth.html')





def chats_(request):
    room_notify = RoomNotification.objects.all()
    return render(request,'chats.html',{'room_notify':room_notify})





def chatroom_(request,pk):
    return render(request,'chatroom.html')