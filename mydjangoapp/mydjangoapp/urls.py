# mydjangoapp/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),  # Include hello app's URLs
]
