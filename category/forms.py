from django.forms import ModelForm
from category.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['name', ]
        exclude = ['slug', ]

