
from django.contrib import admin
from django.urls import path
from woman.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womanlist/', WomanAPIView.as_view())
]
