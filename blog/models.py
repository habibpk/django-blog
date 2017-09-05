from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class category(models.Model):
    cate = models.CharField(max_length=100, verbose_name="Add Category")

    def __str__(self):
        return self.cate

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name


class article(models.Model):
    title = models.CharField(max_length=250)
    disc = models.TextField(verbose_name="Discription")
    cat = models.ForeignKey(category, verbose_name="Category")
    posted = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    img = models.ImageField(verbose_name='Image', blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class comment(models.Model):
    text = models.TextField(verbose_name="Add Comment")
    dated = models.DateTimeField(auto_now_add=True, editable=False)
    art = models.ForeignKey(article, on_delete = models.CASCADE)
