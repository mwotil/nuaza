from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render_to_response
from django import forms
from django.contrib.comments.forms import CommentForm
from django.template import RequestContext
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from marcofucci_utils import fields as marcofucci_fields

TOPIC_CHOICES = (
    ('', '--Select Category--'),
    ('General enquiry', 'General enquiry'),
    ('Bug report', 'Bug report'),
    ('Suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):

    error_css_class = 'error'
    required_css_class = 'required'

    name = forms.CharField(error_messages = {'required':("Your Name is Required")})
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, error_messages = {'required':("Choose a topic")})
    message = forms.CharField(widget=forms.Textarea(), error_messages = {'required':("Message Field can not be empty")})
    email = forms.EmailField(required=True, error_messages = {'required':("Your Email Address is Required")})
    captcha = CaptchaField(output_format=u'%(image)s %(hidden_field)s %(text_field)s', error_messages = {'required':("The captcha field is Required")} )
    #recaptcha = marcofucci_fields.ReCaptchaField()

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words for the message!")
        return message

def __init__(self, *args, **kwargs):
  super(ContactForm, self).__init__(*args, **kwargs)
  if not self.fields['type'].choices[0][0] == '':
    self.fields['type'].choices.insert(0, ('','---------' ) )
