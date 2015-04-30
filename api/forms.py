from models import Photo
from models import AndroidProduct
from django.forms import ModelForm

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
  
class AndroidProductForm(ModelForm):

    class Meta:
        model = AndroidProduct
        
        exclude = ('user','slug',)