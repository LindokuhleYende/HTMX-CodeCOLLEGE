from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:author_id>/', edit_author, name='edit_author'),
     path('user/<int:author_id>/update/', update_user, name='update_user'),
]
