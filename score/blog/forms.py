from django import forms
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError
import Image as pil



#from ajaximage.widgets import AjaxImageWidget
'''class writeform(forms.Form):
	title = forms.CharField(widget = forms.Textarea(attrs={'rows' : 1 , 'cols' : 100, 'name' : 'title'}))
	post = forms.CharField(widget = forms.Textarea(attrs={'id' : 'writer', 'name' : 'text'}))


class AjaxImageUploadForm(forms.Form):
    image = forms.URLField(widget=AjaxImageWidget())
'''
class upload(forms.Form):
	image = forms.ImageField()



