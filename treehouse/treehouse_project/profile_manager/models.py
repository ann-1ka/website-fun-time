from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
#from validators import telephone_validator, color_validator

def user_background_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/profile_background_images/<id>/<filename>
    return 'profile_background_images/{0}/{1}'.format(instance.user.id, filename)

def user_profile_picture_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/profile_pictures/<id>/<filename>
    return 'profile_background_images/{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    email = models.EmailField(blank=False, null=True)
    phone_number = models.CharField(max_length=16) #, validators=[telephone_validator]
    dob = models.DateField(default=date.today)
    display_name = models.CharField(max_length=64, null=True, blank=True)
    bio = models.TextField()
    background_image = models.FileField(upload_to=user_background_path, null=True, blank=True)
    background_color = models.CharField(max_length=8)  #, validators=[color_validator]
    profile_picture = models.FileField(upload_to=user_profile_picture_path, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['dob']

# Source - https://stackoverflow.com/a/58799650
# Posted by Enthusiast Martin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-01, License - CC BY-SA 4.0
class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user_id', 'following_user_id')

class UserBlocked(models.Model):
    user_id = models.ForeignKey("User", related_name="has_blocked", on_delete=models.CASCADE)
    blocked_user_id = models.ForeignKey("User", related_name="blocked_by", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user_id', 'blocked_user_id')


class Notification(models.Model):
    notif_type = models.CharField(max_length=16) #post, message, update, follow
    subject = models.CharField(max_length=64) #user just posted, user sent you a message, user followed
    content = models.TextField() #post caption, message content