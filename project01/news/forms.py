from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'id': "title",
                                            "placeholder": "Enter title",
                                            "name": "title"}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             "rows": "5"})
        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'id': "title",
                                                                          "placeholder": "Enter title",
                                                                          "name": "title"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': "email",
                                                            "placeholder": "Enter email",
                                                            "name": "email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           "rows": "5"}))
    cc = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input",
                                                                              "type": "checkbox",
                                                                              "name": "remember"}))
