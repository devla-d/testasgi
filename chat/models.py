import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email       = models.EmailField( blank=True,null=True)
    username    = models.CharField(max_length=50,unique=True)
    

    def __str__(self):
        return self.username



class Room(models.Model):
    users = models.ManyToManyField(Account,blank=True,related_name='room_users')
    uri = models.CharField(max_length=50)




class RoomMessage(models.Model):
    """
    Chat message created by a user inside a Room
    """
    user                = models.ForeignKey(Account, on_delete=models.CASCADE)
    room                = models.ForeignKey(Room, on_delete=models.CASCADE)
    timestamp           = models.DateTimeField(auto_now_add=True)
    content             = models.TextField(unique=False, blank=False,)





    def __str__(self):
        return self.content
    
    def to_json(self):
        """deserialize message to JSON."""
        return {'user': deserialize_user(self.user), 'content': self.content}




def deserialize_user(user):
    """Deserialize user instance to JSON."""
    return {
        'id': user.id, 'username': user.username,
    }



class RoomNotification(models.Model):

    # Who the notification is sent to
    target 						= models.ForeignKey(Account, on_delete=models.CASCADE, related_name="send_to")

    # The user that the creation of the notification was triggered by.
    from_user 					= models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="message_from_user")


    # statement describing the notification  
    verb 						= models.CharField(max_length=255, unique=False, blank=True, null=True)

    # When the notification was created/updated
    timestamp 					= models.DateTimeField(auto_now_add=True, null=True, blank=False)

    room                      =  models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name="thread")

    # Some notifications can be marked as "read"
    unread_count					= models.IntegerField(default=0)


    class Meta:
        ordering = ['-timestamp']



    def __str__(self):
        return f"{self.target.username}"