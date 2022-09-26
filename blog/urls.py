from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),

    path('choice/', views.SampleChoiceAddView.as_view(), name='choice'),
    path('test/', views.BlogTestView.as_view(), name='test'),
]
