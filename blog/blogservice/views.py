import django.utils.timezone
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Posts, Likes, Users, Comments
from .forms import AddPostForm, AddCommentForm

blocks = [
    {'name': 'Blog', 'link': '/'},
    {'name': 'About', 'link': '/about'},
]


def index(request):
    v = request.COOKIES.get('auth')
    if v:
        auth_status = True
    else:
        auth_status = False
    posts = Posts.objects.all()
    return render(request, "blogservice/index.html", {
        "posts": posts,
        'title': 'Main page',
        'blog_title': "SITE's NAME",
        'blocks': blocks,
        'is_authenticated': auth_status,
        })


def check_unique_login(request, login):
    users = Users.objects.filter(login=login)
    if users:
        return HttpResponse(status=203)
    else:
        return HttpResponse(status=204)


def check_post_liked(request, user_id, post_id):
    if not Likes.objects.filter(user_id=user_id, post_id=post_id):
        new_like = Likes(user_id=user_id, post_id=post_id)
        new_like.save()
        post = Posts.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=204)


def show_post(request, id,):
    v = request.COOKIES.get('auth')
    auth_status = True if v else False
    if v:
        v = v.split()
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form_2 = Comments(
                post_id=id,
                content=form.data['content'],
                author=v[0],
            )
            form_2.save()
            return redirect('post_show', id)
    else:
        comments = Comments.objects.filter(post_id=id)
        try:
            posts = Posts.objects.get(pk=id)
            posts.post_views += 1
            try:
                like = Likes.objects.filter(post_id=posts.id)[0]
                current_user = Users.objects.get(login=v[0])

                if like.user_id == current_user.id:
                    is_liked = True
                else:
                    is_liked = False
            except ObjectDoesNotExist:
                is_liked = False
            except IndexError:
                is_liked = False
            except TypeError:
                is_liked = None
            author = Users.objects.get(id=posts.post_author_id)
            posts.save()
            if v:
                author_of_post = True if v[0] == author.login else False
                current_user = Users.objects.get(login=v[0])
                user = current_user.id
            else:
                author_of_post = False
                user = None
            return render(request, "blogservice/post.html",
                          {"post_id": id,
                           'post_info': posts.id,
                           'title': 'Post ' + str(posts.id),
                           'blog_title': "SITE's NAME",
                           'blocks': blocks,
                           'post_title': posts.title,
                           'post_likes': posts.likes,
                           'post_content': posts.content,
                           'post_author': author.login,
                           'post_preview': posts.preview,
                           'form': AddCommentForm(),
                           'comments': comments,
                           'is_authenticated': auth_status,
                           'author_of_post': author_of_post,
                           'user_id': user,
                           'is_liked': is_liked,
                           })
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/')


def edit_post(request, id):
    v = request.COOKIES.get('auth')
    auth_status = True if v else False
    posts = Posts.objects.get(pk=id)
    author = Users.objects.get(id=posts.post_author_id)
    if request.method == 'POST':
        print(posts.id)
        posts.title = request.POST.get('title')
        posts.content = request.POST.get('content')
        print(posts.content)
        posts.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,
                      "blogservice/edit-post.html",
                      {
                        "post_id": id,
                        'id': posts.id,
                        'title': 'Post ' + str(posts.id),
                        'blog_title': "SITE's NAME",
                        'blocks': blocks,
                        'post_title': posts.title,
                        'post_content': posts.content,
                        'post_author': author.login,
                        'is_authenticated': auth_status,
                        'form': AddPostForm()
                       }
                      )


def create(request):
    v = request.COOKIES.get('auth')
    if v:
        auth_status = True
    else:
        auth_status = False

    post_author = request.COOKIES.get('auth')
    post_author = post_author.split()
    author = Users.objects.get(login=post_author[0])

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form_2 = Posts(
                post_author_id=author.id,
                content=form.data['content'],
                title=form.data['title'],
                preview=form.files['preview'],
            )
            form_2.save()
            return redirect('main')
    else:
        return render(request, "blogservice/create.html", {
                    'title': 'Main page',
                    'blog_title': "SITE's NAME",
                    'blocks': blocks,
                    'form': AddPostForm(),
                    'is_authenticated': auth_status,
                    })


def about(request):
    user = Users.objects.all()
    posts = Posts.objects.all()
    return render(request, "blogservice/about.html", {
        "posts": posts,
        'title': 'Main page',
        'blog_title': "SITE's NAME",
        'blocks': blocks,
        'username': user,
                    })


def personal_area(request):
    return render(request, 'blogservice/personal_area.html', {
        'title': 'Personal area',
        'blog_title': "SITE's NAME",
        'blocks': blocks,
    })


def base(request):
    return render(request, 'blogservice/base.html', {
        'title': 'Main page',
        'blog_title': "SITE's NAME",
        'blocks': blocks,
    })


def sign_in(request):
    try:
        user = Users.objects.get(login=request.POST.get("login"))
        login = user.login
        pw = user.password
        entered_pw = request.POST.get('password')
        if pw == entered_pw:
            response = HttpResponseRedirect('/')
            response.set_cookie('auth', str(login) + ' ' + str(pw))
            return response
        else:
            return render(request, 'blogservice/sign-in.html')
    except ObjectDoesNotExist:
        return render(request, 'blogservice/sign-in.html',)


def log_out(request):
    response = redirect('main')
    response.delete_cookie('auth')
    return response


def sign_up(request):
    if request.method == "POST":
        user = Users()
        user.email = request.POST.get("email")
        user.login = request.POST.get("login")
        user.password = request.POST.get("password")
        user.join_date = django.utils.timezone.now()
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'blogservice/sign-up.html',)
