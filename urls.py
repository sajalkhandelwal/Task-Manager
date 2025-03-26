from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('task/', include('task.urls')),
    path('admin/', admin.site.urls),
]