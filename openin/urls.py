from django.conf.urls import url
from . import views


urlPatterns = [
        url('', views.index, name='home')

]
