from django.conf.urls import url

from . import views
app_name='accounts'


urlpatterns=[
url(r'^sign/$',views.sign,name='sign'),
url(r'^login/$',views.log,name='login'),
url(r'^logout/$',views.logoutview,name='logout'),
]
