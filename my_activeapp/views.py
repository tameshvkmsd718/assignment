#from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')


def user_list(request):
    users = User.objects.all()
    return render(request, 'my_activeapp/user_list.html', {'users': users})


def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        User.objects.create(name=name, email=email)
        return redirect('user_list')
    return render(request, 'my_activeapp/new_user.html')



def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User not found")
    return render(request, 'my_activeapp/user_detail.html', {'user': user})
