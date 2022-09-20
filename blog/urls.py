from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('test/', views.BlogTestView.as_view(), name='test'),
]
