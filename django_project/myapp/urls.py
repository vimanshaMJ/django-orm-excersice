from django.urls import path
from .views import ( AnnotationPostView, BulkCreateUserView, CommentListView, DistinctUsersView, HomeView, PostFirstView, 
    PostGetOrCreateView, PostLastView, PostListView, ProfileListView, UserListView, UserByEmailView, 
    UsersByExcludeUsernameView, UserByIdView, CreateUserView, UserCountView, ProfileUpdateOrCreateView, 
    ReversePostsView,
    PostValuesView, PostValuesListView, CommentsSelectRelatedView,
    UsersUsingView, PostExistsView, UpdateUserView, DeleteCommentView )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/email/<str:email>/', UserByEmailView.as_view(), name='user_by_email'),
    path('users/exclude/<str:username>/', UsersByExcludeUsernameView.as_view(), name='users_by_exclude_username'),
    path('users/<int:id>/', UserByIdView.as_view(), name='user_by_id'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/bulk_create/', BulkCreateUserView.as_view(), name='bulk_create_user'),
    path('users/count/', UserCountView.as_view(), name='user_count'),
    path('users/distinct/', DistinctUsersView.as_view(), name='distinct_authors'),
    path('users/using/<str:db_alias>/', UsersUsingView.as_view(), name='users_using'),
    path('users/<int:id>/update/', UpdateUserView.as_view(), name='update_user'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/get_or_create/', PostGetOrCreateView.as_view(), name='post_get_or_create'),
    path('posts/annotate_comments_count/', AnnotationPostView.as_view(), name='annotate_comments_count'),
    path('posts/first/', PostFirstView.as_view(), name='post_first'),
    path('posts/last/', PostLastView.as_view(), name='post_last'),
    path('posts/order_by/', PostListView.as_view(), name='post_order_by'),
    path('posts/reverse/', ReversePostsView.as_view(), name='reverse_posts'),
    path('posts/values/', PostValuesView.as_view(), name='post_values'),
    path('posts/values_list/', PostValuesListView.as_view(), name='post_values_list'),
    path('posts/exists/', PostExistsView.as_view(), name='post_exists'),

    path('profile/', ProfileListView.as_view(), name='profile_list'),
    path('profile/update_or_create/', ProfileUpdateOrCreateView.as_view(), name='profile_update_or_create'),

    path('comments/select_related/', CommentsSelectRelatedView.as_view(), name='comments_select_related'),
    path('comments/',CommentListView.as_view(), name='comments_list'),
    path('comments/<int:id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),

]
