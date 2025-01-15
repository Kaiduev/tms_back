from django.contrib import admin
from django.urls import path, include

from .swagger import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls'), name="tasks"),
    path('api/users/', include('users.urls'), name="users")
]
urlpatterns += docs_urls
