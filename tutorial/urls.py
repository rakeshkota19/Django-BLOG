from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from tutorial.quickstart import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from articles import views as article_views
from django.conf import settings
from django.http import HttpResponse
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/',admin.site.urls),
    url(r'^about/',views.about),
    url(r'^$',article_views.articlelist,name='home'),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
