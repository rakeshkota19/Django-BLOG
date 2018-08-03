from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.http import HttpResponse
app_name='articles'
urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^about/',views.about),

    url(r'^$',views.articlelist,name="list"),
    #named capturing group
    url(r'^create/$',views.create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.articledetail,name="detail"),

]
