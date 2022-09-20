from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='index'),
]
