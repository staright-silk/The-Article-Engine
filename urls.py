from django.urls import path
from .views import search_view

urlpatterns=[
    path("", search_view, name ="search"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path("admin/", admin.site.urls),
    path("", include("searchapp.urls"))
]