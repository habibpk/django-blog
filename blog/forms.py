from django import forms
from .models import article, comment, category

class ArticleForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = article
        fields = [
            "title", "disc", "cat"
        ]

class CommentForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = comment
        fields = [
            "text"
        ]

class CategoryForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = category
        fields =[
            "cate"
        ]

class CateForm(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = category
        fields =[
            "cate"
        ]
        labels = {
            "cate": "Update Category"
        }
