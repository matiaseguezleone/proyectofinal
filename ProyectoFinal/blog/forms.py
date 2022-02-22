from django import forms
from .models import Post    

class postForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # content = forms.CharField(widget=forms.Textarea)
    # thumbnail = forms.ImageField()
    # author = forms.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        model = Post
        fields = ('title', 'content', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }