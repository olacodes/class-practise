from django.urls import path
from .views import ForumListView, register, RegisterView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', ForumListView.as_view(), name='forums'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
