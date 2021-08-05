from django.urls import path
from . import views

app_name = 'quote'
urlpatterns = [
    path('quote-main/', views.HomeView.as_view(), name='main'),
    path('quote-list/', views.QuoteListView.as_view(), name='quote-list'),
    path('quote-create/', views.QuoteCreateView.as_view(), name='quote-create'),
    path('<int:pk>/detail', views.QuoteDetailView.as_view(), name='quote-detail'),
    path('<int:pk>/edit', views.QuoteEditView.as_view(), name='quote-edit'),
    path('<int:pk>/del', views.QuoteDeleteView.as_view(), name='quote-del'),
    path('<slug:slug>/mail', views.send_email_quote, name='quote-mail'),
]
