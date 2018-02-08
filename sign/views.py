from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
        return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username   #将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

#发布会管理
@login_required()
def event_manage(request):
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user":username})

def event_manage(request):
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user":username})