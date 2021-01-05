from django.urls import path
from .views import ProfileListView, ProfileDetailView, RegisterView, ProfileUpdateView

urlpatterns =[
    path('', ProfileListView.as_view(), name='user-list'),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='user-detail'),
    path('profile-update/<slug:slug>', ProfileUpdateView.as_view(), name='profile-update')]
