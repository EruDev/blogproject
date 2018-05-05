import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra', # 包含很多拓展
                                      'markdown.extensions.codehilite', # 语法高亮
                                      'markdown.extensions.toc', # 允许我们自动生成目录
                                  ])

    comment_list = post.comment_set.all()
    form = CommentForm()
    context = {
        'form': form,
        'post': post,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})
