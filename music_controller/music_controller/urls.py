from django.contrib import admin
from django.urls import path, include

# root url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
]
