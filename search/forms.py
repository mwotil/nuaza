from Nuaza.search.models import SearchTerm
from django import forms
from django.forms import ModelForm, Textarea


class SearchForm(forms.ModelForm):
	""" form class for accepting search terms """
	class Meta:
		model = SearchTerm
		widgets = {'q': forms.TextInput(attrs={'class':'search-field'}),'cat': forms.Select(attrs={'class':'search-cat'}),}
 
		
	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		default_text = 'Search Products'
		self.fields['q'].widget.attrs['value'] = default_text
		self.fields['q'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"
		self.fields['cat'].empty_label = "All Categories"
        
	include = ('q','cat')
