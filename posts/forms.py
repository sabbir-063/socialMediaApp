from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'input-class', 'placeholder': 'Write your post here...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-class'}),
        }
