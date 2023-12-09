from django import forms
from django.core.exceptions import ValidationError
from django.http import request
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from Blog.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'summary', 'content', 'main_photo')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'summary': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control back-drop'}),
            'main_photo': forms.FileInput(attrs={'class': 'upload__file'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 0 >= len(title) > 50:
            raise ValidationError('Title must contain from 1 to 50 characters')
        return title.replace('\n', '<br>')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'main_photo', 'summary', 'content', 'is_published', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'slug': forms.TextInput(attrs={'class': 'form-control back-drop'}),
            'summary': forms.Textarea(attrs={'class': 'form-control back-drop', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control back-drop'}),
            'main_photo': forms.FileInput(attrs={'class': 'upload__file'}),
            'is_published': forms.CheckboxInput(attrs={'class': "form-check-input",
                                                       'type': "checkbox",
                                                       'role': "switch"}
                                                )
        }
        labels = {'is_published': 'Publish'}








