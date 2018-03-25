from django.conf.urls import url
from . import views

urlpatterns = [
    url('$', views.gettingstarted, name='Warming Up Bitches!'),
]
