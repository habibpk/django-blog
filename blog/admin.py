from django.contrib import admin
from .models import article, category, comment, Tag

admin.site.register(article)
admin.site.register(category)
admin.site.register(comment)
admin.site.register(Tag)