from django.urls import path
from . import views

app_name = 'followup'
urlpatterns = [
    path('new/', views.CreateNew.as_view(), name='new'),
    path('<slug:slug>/', views.FollowUpDetailView.as_view(), name='detail'),
    path('<slug:slug>/delete/', views.FollowUpDeleteView.as_view(), name='delete')
]
