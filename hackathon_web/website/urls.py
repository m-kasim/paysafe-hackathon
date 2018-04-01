# URL router
from django.conf.urls import url

# NOTE: Import all [templates] manually here
from .views import index, detail
##from . import views

urlpatterns = [
    url(r'^$',                  index.index,                    name='index'),
    url(r'^detail',             detail.detail,                  name='detail'),
]