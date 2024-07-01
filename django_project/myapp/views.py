import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User, Profile, Post, Comment, Tag, PostTag
from django.db.models import Sum, Avg, Count, Max, Min

# Create your views here.

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hey there! This is a Django ORM exercise 01.")


# User views
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        users_list = list(users.values())
        return JsonResponse(users_list, safe=False)

class UserByEmailView(View):
    def get(self, request, email):
        user = User.objects.filter(email=email)
        user_list = list(user.values())
        return JsonResponse(user_list, safe=False)

class UsersByExcludeUsernameView(View):
    def get(self, request, username):
        user = User.objects.exclude(username=username)
        user_list = list(user.values())
        return JsonResponse(user_list, safe=False)

class UserByIdView(View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return JsonResponse(user_data)

@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        user.save()
        return JsonResponse({"message": "User created successfully!"}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class BulkCreateUserView(View):
    def post(self, request):
        data = json.loads(request.body)
        users = []
        for user in data:
            users.append(User(
                username=user['username'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name']
            ))
        User.objects.bulk_create(users)
        return JsonResponse({"message": "Users created successfully!"}, status=201)
    
class UserCountView(View):
    def get(self, request):
        count = User.objects.all().count()
        return JsonResponse({"count": count}, status=200)
    

# Post views
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        posts_list = list(posts.values())
        return JsonResponse(posts_list, safe=False)
    

class PostGetOrCreateView(View):
    def get(self, request):
        title = request.GET.get('title')
        author_id = request.GET.get('author_id')
        author = get_object_or_404(User, id=author_id)
        post, created = Post.objects.get_or_create(title=title, author=author)
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author_id': post.author.id,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        }
        return JsonResponse(post_data)
    

# Profile views
class ProfileListView(View):
    def get(self, request):
        profiles = Profile.objects.all()
        profiles_list = list(profiles.values())
        return JsonResponse(profiles_list, safe=False)
    
@method_decorator(csrf_exempt, name='dispatch')
class ProfileUpdateOrCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = get_object_or_404(User, id=data['user_id'])
        profile, created = Profile.objects.update_or_create(
            user=user,
            defaults={
                'user_id': data['user_id'],
                'bio': data['bio'],
                'birth_date': data['birth_date']
            }
        )
        return JsonResponse({"message": "Profile updated/created successfully!"}, status=200)
    
class AnnotationPostView(View):
    def get(self, request):
        posts = Post.objects.annotate(Count('comment'))
        posts_list = list(posts.values())
        return JsonResponse(posts_list, safe=False)
    
class PostFirstView(View):
    def get(self, request):
        post = Post.objects.first()
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author_id': post.author.id,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        }
        return JsonResponse(post_data)

class PostLastView(View):
    def get(self, request):
        post = Post.objects.last()
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author_id': post.author.id,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        }
        return JsonResponse(post_data)
    
    