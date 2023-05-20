from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Comment,Book

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signup')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/signup.html")

def login1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:login')
    return render(request,"web/login.html")

def shoplist(request):
    books =Book.objects.all()
    context= {
        "books" : books,
    }
    return render(request, 'web/shoplist.html',context)

def detail(request):
      
    return render(request, 'web/shop-detail.html')

# @login_required
# def comment_submit(request):
#     if request.method == 'POST':
#         content = request.POST['content']
#         author = request.user
#         comment = Comment(content=content, author=author)
#         comment.save()
#         return redirect('shop')  # Redirect to the comments list page

#     return render(request, 'web/comment_submit.html')