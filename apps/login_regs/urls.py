from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^create_user$', views.create_user),
    url(r'^login$', views.login),
    url(r'^login_user$', views.login_user),
    url(r'^logout_user$', views.logout),
]
