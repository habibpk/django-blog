from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import article, category
from .forms import ArticleForm, CommentForm, CategoryForm, CateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages


def index(request):
    queryset = article.objects.filter().order_by('-pk')
    paginator = Paginator(queryset, 4)  # Show 25 contacts per page
    Title = "Latest Posts"
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    context = {
        'data':data,
        'Title':Title,
    }
    return render(request, 'blog/index.html', context)

def post_create(request):
    form = ArticleForm(request.POST or None)
    msg = "Welcome to site"
    context = {
        'Title': msg,
        'form': form,
    }
    if form.is_valid():
        form.save()
        context = {
            'Title': 'Thank you',
        }

    return render(request, 'blog/create.html', context)

def detail(request, pk):
    try:
        num = article.objects.get(pk)
    except article.DoesNotExist:
        raise Http404("Article Not Found")
    context = {
        'num': num,
    }
    return render(request, 'blog/detail.html', context)

class DetailView(generic.DetailView):
    model = article
    template_name = 'blog/detail.html'

class ArticleCreate(CreateView):
    model = article
    fields = ['title', 'cat', 'img', 'disc', 'tags']

class ArticleUpdate(UpdateView):
    model = article
    fields = ['title', 'cat', 'img', 'disc', 'tags']

class ArticleDelete(DeleteView):
    model = article
    success_url = reverse_lazy('blog:index')


def search(request):
    all_data = article.objects.all()
    query = request.GET.get("q")
    if query:
        all_data = all_data.filter(Q(title__contains=query))
        if all_data:
            Title = "Search Result"
        else:
            Title = 'No Record Found'
        context = {
            'all_data': all_data,
            'Title': Title,
             'query': query,
        }

    return render(request, 'blog/search.html', context)

def Categories(request):
    get_cat = category.objects.all()
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Category added successfully')
    context = {
        'get_cat': get_cat,
        'form': form,
    }
    return render(request, 'blog/category.html', context)

def cat_detail(request, pk):
    post_cat = get_object_or_404(category, pk=pk)
    article_list = article.objects.filter(cat=post_cat)
    context = {
        'post_cat': post_cat,
        'article_list':article_list
    }
    return render(request, 'blog/post_cat.html', context)

def add_comment(request, pk):
    post = get_object_or_404(article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.art = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {'form': form,}
    return render(request, 'blog/add_comment.html', context)

def cat_update(request, pk):
    page = get_object_or_404(category, pk=pk)
    if request.method == 'POST':
        form = CateForm(request.POST or None, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
    else:
        form = CateForm(instance=page)
    context = {'form': form,}
    return render(request, 'blog/update_comment.html', context)