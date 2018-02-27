from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import User, Wish
from django.contrib import messages
import re

def index(request):

    return render(request, 'exam/index.html')
def register(request):
    
    return redirect('/')

def login(request):
    
    # if User.objects.filter(username=postData['username']).exists() and User.objects.filter(password=postData['password']).exists():
    #     return redirect('/')
    # else:

        return redirect('/dashboard')

def create(request):
    errors = User.objects.validateUser(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')
    else:
        new_user = User.objects.create(

        name = request.POST['name'], 
        username = request.POST['username'],
        password = request.POST['password'],
        date_hired = request.POST['date_hired'])

        request.session['user_id'] =new_user.id

        return redirect('/dashboard')

def dashboard(request):

    my_wish = Wish.objects.filter(wishers = User.objects.get(id = request.session['user_id']))
    all_wish = Wish.objects.all()
    user_name = User.objects.get(id=request.session['user_id']).name
    all_other_wishes = all_wish.difference(my_wish)
    
    context  = {
        'my_wish' : my_wish,
        'other_wishes' : all_other_wishes,
        'user_name' : user_name 
    }
    return render(request,'exam/dashboard.html', context)

def add(request):
     return render(request, 'exam/add.html')

def addWish(request):
    response = Wish.objects.validateWish(request.POST, request.session['user_id'])

    return redirect('/dashboard', response)

def show(request, wish_id):

    thisWish = Wish.objects.get(id=wish_id)
    # others = thisWish.wishers.all().exclude()
    others = User.objects.filter(wish_joined=thisWish).exclude(added_joined=thisWish)

    context = {
        'thisWish' : thisWish,
        'others' : others
    }

    return render(request, 'exam/show.html', context)

def createJoin(request, wish_id):

    user = User.objects.get(id = request.session['user_id'])
    wish = Wish.objects.get(id = wish_id)
    wish.wishers.add(user)

    return redirect('/dashboard')

def delete(request):
    
    return redirect('/dashboard')
def destroy(request, wish_id):
    Wish.objects.filter(id = wish_id).delete()
    return redirect('/dashboard')

