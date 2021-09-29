from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('greener.urls')),
    path('auth/', include('authentication.urls')),
    path('user/', include('host.urls')),
    path('admin/', admin.site.urls),
]
