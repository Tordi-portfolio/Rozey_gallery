from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "category",
            "title",
            "image",
            "short_description",
            "description",
            "artist",
            "featured",
        ]

        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "short_description": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                }
            ),
            "artist": forms.TextInput(attrs={"class": "form-control"}),
            "featured": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }