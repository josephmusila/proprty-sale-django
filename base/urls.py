from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path("", views.index,name="home"),
    path("details/<str:pk>/", views.details,name="details"),

]