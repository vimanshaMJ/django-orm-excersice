from django.urls import path
from .views import  AnnotationPostView, BulkCreateUserView, HomeView, PostFirstView, PostGetOrCreateView, PostLastView, PostListView, ProfileListView, UserListView, UserByEmailView, UsersByExcludeUsernameView, UserByIdView, CreateUserView, UserCountView, ProfileUpdateOrCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/email/<str:email>/', UserByEmailView.as_view(), name='user_by_email'),
    path('users/exclude/<str:username>/', UsersByExcludeUsernameView.as_view(), name='users_by_exclude_username'),
    path('users/<int:id>/', UserByIdView.as_view(), name='user_by_id'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/bulk_create/', BulkCreateUserView.as_view(), name='bulk_create_user'),
    path('users/count/', UserCountView.as_view(), name='user_count'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/get_or_create/', PostGetOrCreateView.as_view(), name='post_get_or_create'),
    path('posts/annotate_comments_count/', AnnotationPostView.as_view(), name='annotate_comments_count'),
    path('posts/first/', PostFirstView.as_view(), name='post_first'),
    path('posts/last/', PostLastView.as_view(), name='post_last'),

    path('profile/', ProfileListView.as_view(), name='profile_list'),
    path('profile/update_or_create/', ProfileUpdateOrCreateView.as_view(), name='profile_update_or_create'),



   

]
