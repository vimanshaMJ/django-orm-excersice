import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Post, Profile, Comment, Tag, PostTag
from django.db.models import Count, Sum, Avg
from django.views.decorators.http import require_http_methods

# Create your views here.

def home(request):
    return HttpResponse("Hey there! This is a Django ORM exercise 01.")


def user_list(request):
    users = User.objects.all()
    users_list = list(users.values())
    return JsonResponse(users_list, safe=False)

def users_by_email(request, email):
    user = User.objects.filter(email=email)
    user_list = list(user.values())
    return JsonResponse(user_list, safe=False)

def users_by_exclude_username(request, username):
    user = User.objects.exclude(username=username)
    user_list = list(user.values())
    return JsonResponse(user_list, safe=False)

def users_by_id(id):
    user = User.objects.get(id=id)
    user_list = list(user.values())
    return JsonResponse(user_list, safe=False)

