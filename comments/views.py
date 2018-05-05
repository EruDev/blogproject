from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from blog.models import Post


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context)
    return redirect(post) # 这里可以直接重定向post, 是因为 blog/models下的Post 重写了get_absolute_url 方法



