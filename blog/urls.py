from django.conf.urls import url
from .import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^category/$', views.Categories, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.cat_detail, name='cat_detail'),
    url(r'^category/(?P<pk>[0-9]+)/update/$', views.cat_update, name='cat_update'),
    url(r'^create/$', views.post_create, name='article-form'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^detail/(?P<pk>[0-9]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^add/$', views.ArticleCreate.as_view(), name='article-add'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ArticleUpdate.as_view(), name='article-update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ArticleDelete.as_view(), name='article-delete'),
]



