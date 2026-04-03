from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import Post

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400 outline-none',
                'placeholder':field.label
                })

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content","featured_image","is_published"]


    widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border rounded px-3 py-2'
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'w-full'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4'
            }),
        }