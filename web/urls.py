from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.views.generic import TemplateView
from .views import HomeView, ContactCreate
from django.views.generic.base import RedirectView

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
    url(r'^sass-resources', TemplateView.as_view(template_name='sass-resources.html')),
    url(r'^less-resources', TemplateView.as_view(template_name='less-resources.html')),
    url(r'^color-resources', TemplateView.as_view(template_name='color-resources.html')),
    url(r'^flex-resources', TemplateView.as_view(template_name='flex-resources.html')),
    url(r'^demo/stickydemo', TemplateView.as_view(template_name='demos/sticky.html')),
    url(r'^lodigazebo', TemplateView.as_view(template_name='lodigazebo.html')),
    url(r'^contact', ContactCreate.as_view(), name="contact"),
    url(r'^blog/dotcmsmaplists', RedirectView.as_view(url='http://bradrice.com/thoughts/posts/dotcms-map-lists', permanent=True)),
]
