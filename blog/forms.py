from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    Creates a blog form
    """
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
