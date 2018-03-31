# URL router
from django.conf.urls import url

# NOTE: Import all [templates] manually here
from .views import index
##from . import views

urlpatterns = [
    url(r'^$',                  index.index,                        name='index'),
]