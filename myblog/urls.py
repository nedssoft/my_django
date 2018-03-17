from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$', views.my_profile, name='my_profile'),
    url('^news$', views.post_list, name="post_list"),
]
