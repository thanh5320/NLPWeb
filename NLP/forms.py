from django import forms
 
class Img(forms.Form):
    img = forms.ImageField(label='Hình ảnh')