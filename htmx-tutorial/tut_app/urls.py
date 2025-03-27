from . import views
from django.urls import path


urlpatterns = [
    path('index/', views.example, name='example'),
    path('sample-post/', views.sample_post, name='sample-post'),
]