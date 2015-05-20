from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    # Examples:
     url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^resume', TemplateView.as_view(template_name='resume.html')),
    url(r'^portfolio', TemplateView.as_view(template_name='portfolio.html')),
]
