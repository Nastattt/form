from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, NewsForm

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'Новость {title}<br>'
                            f'Контент {content} <br>'
                            f'Вид {is_published}, {category}')
    else:
        form = NewsForm()
        return render(request, 'app/news.html', context={'form': form})

def index(request):
    if request.method == "POST":
        title = request.POST.get('name')
        content = request.POST.get('age')
        is_published = request.Post.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'Новость {title}<br>'
                            f'Контент {content} <br>'
                            f'Вид {is_published}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})
def myForm(request):
    return render(request, 'app/form.html')

def user(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse(f'User {name},Age {age}')