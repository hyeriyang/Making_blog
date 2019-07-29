from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk = blog_id ) #몇번 블로그 객체를 이용자가 원하는가

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터 베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def album(request):
    blogs = Blog.objects
    return render(request, 'album.html', {'blogs':blogs})
