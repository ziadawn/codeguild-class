
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Blog, Comment                # the . is the current working directory


def index(request):
    # return HttpResponse('ok')       # render, which I had before, is just for templates
    posts = Blog.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    comments = Comment.objects.filter(post=post)
    # return HttpResponse(post.body)

    if request.method == 'POST':
        body = request.POST['body']
        comment = Comment(body=body, commenter=request.user, post=post)
        comment.save()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments})


def write_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        write = Blog(title=title, body=body, poster=request.user)
        write.save()
        HttpResponseRedirect(reverse('blog:index'))
    return render(request, 'blog/write_post.html')

