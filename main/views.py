from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from main.forms import NewsForm, RegisterForm
from main.models import News
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        news_list = News.objects.all()
    else:
        news_list = News.objects.filter(user=request.user)

    context = {
        'npm': '240123456',
        'name': request.user.username,
        'class': 'PBP A',
        'news_list': news_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

    return render(request, "main.html", context)
@login_required(login_url='/login')
def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_news.html", context)

@login_required(login_url='/login')
def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()

def show_xml(request):
     news_list = News.objects.all()
     xml_data = serializers.serialize("xml", news_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    news_list = News.objects.all()

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
   try:
       news_item = News.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except News.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, news_id):
   try:
       news_item = News.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [news_item])
       return HttpResponse(json_data, content_type="application/json")
   except News.DoesNotExist:
       return HttpResponse(status=404)

def register(request):
    role = request.GET.get("role", "pelanggan")

    if role == "penyelenggara":
        role_title = "Daftar sebagai Penyelenggara"
    else:
        role_title = "Daftar sebagai Pelanggan"

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["full_name"]
            user.save()

            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")

    context = {
        "form": form,
        "role": role,
        "role_title": role_title,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    form.fields['username'].widget.attrs.update({
        'placeholder': 'Masukkan username'
    })
    form.fields['password'].widget.attrs.update({
        'placeholder': 'Masukkan password'
    })

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))            
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def choose_role(request):
    return render(request, "choose_role.html")