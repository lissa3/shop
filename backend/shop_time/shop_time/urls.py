"""shop_time app
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    url('', include('social_django.urls', namespace='social')),
    url('auth/', include('djoser.social.urls')),
    path('api/v1/categories/',include('categories.urls'))
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]