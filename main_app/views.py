from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Show
from .form import ShowForm

def home(request):
    print('HOME PAGE')
    return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')

def shows(request):
    shows = Show.objects.all()
    return render(request, 'shows_list.html', {'shows': shows})

@login_required(login_url='/login/')
def show_create(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            show = form.save()
            return redirect('profile')
    else:
        form = ShowForm()
    context = {'form': form, 'header': 'Add new tv show', 'user': request.user}
    return render(request, 'show_form.html', context)

@login_required(login_url='/login/')
def show_edit(request, pk):
    show = Show.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save()
            return redirect('shows')
    else: 
        form = ShowForm(instance=show)
    return render(request, 'show_form.html', {'form': form})

def show_delete(request, pk):
    # Show.objects.get(pk=pk).delete()
    show = Show.objects.get(pk=pk)
    if show.user_id == request.user.id:
        show.delete()
    print(show,request.user, 'REQUEST')
    return redirect('shows')

def login_page(request):
    return render(request, 'login_form.html')

def logout_view(request):
    logout(request)
    return redirect('shows')

def profile_show(request):
    if request.user.is_authenticated:
        shows = Show.objects.filter(user_id=request.user.id)
        return render(request, 'profile.html', {'shows': shows})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request, 'profile.html')
        else:
            print("SOMETHING WENT WRONG WITH LOGIN")
            return redirect('login_page')
