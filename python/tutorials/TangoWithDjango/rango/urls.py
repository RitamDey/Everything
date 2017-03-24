from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/', views.about, name="about"),
    url(r'^$', views.index, name="index"),
]
