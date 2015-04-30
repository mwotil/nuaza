from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField
#from phonenumber_field.modelfields import PhoneNumberField
from south.modelsinspector import add_introspection_rules
from Nuaza.checkout.models import BaseOrderInfo

add_introspection_rules([], ["^stdimage\.fields\.StdImageField"])


class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, unique=True)
    First_Name = models.CharField(null=True, blank=True,max_length = 25)
    Last_Name = models.CharField(null=True, blank=True, max_length = 25)
#    Address_1 = models.CharField(max_length = 25)
#    Address_2 = models.CharField(null=True, blank=True, max_length = 25)
    userImg = StdImageField(upload_to = 'images/users', null=True, blank=True, size=(100, 100, True))
    url = models.URLField(null=True, blank=True)
#    phone_number = models.IntegerField(null=True, blank=True)
#    phone_number = PhoneNumberField(null=True, blank=True)
#    Mobile_Phone_Contact = models.IntegerField(help_text="For Example 256772123456")
#    Office_Phone_Contact = models.IntegerField(help_text="For Example 256772123456")
#    Email_Address = models.EmailField()
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField(null=True, blank=True)

    
    def __unicode__(self):
        return 'User Profile for: ' + self.user.username

