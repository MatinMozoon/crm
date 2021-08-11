from django.urls import path
from . import views

app_name = 'organization'
urlpatterns = [
    path('new/', views.CreateNew.as_view(), name='new'),
    path('<slug:slug>/', views.OrganizationDetailView.as_view(), name='detail'),
    path('edit/<slug:slug>/', views.OrganizationEditView.as_view(), name='edit'),
    path('<slug:slug>/delete/', views.OrganizationDeleteView.as_view(), name='delete')
]
