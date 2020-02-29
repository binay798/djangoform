from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('',views.home,name='home'),
    path('result/',views.add_post,name='add_post'),
]