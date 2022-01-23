from django import forms

class postForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    # thumbnail = forms.ImageField()
    # author = forms.ForeignKey(User, on_delete=models.CASCADE)
    
