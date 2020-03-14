from django.contrib import admin
from django.urls import path, include
from views import post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('/', views.post_detail, name='post_detail'),

]