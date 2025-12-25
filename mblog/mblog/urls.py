
from django.contrib import admin
from django.urls import path, include
from mysite.views import homepage, showpost


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),
]
