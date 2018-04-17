from django.conf.urls import url

from sprintercarsapp.views import BaseView, IndexView, ProductsView, ContactView, AboutView, DetailView, PartnersView, \
    search, ContactFormView

urlpatterns = [
    url(r'^base/$', BaseView.as_view(), name='base'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^contact-us/$', ContactView.as_view(), name='contact'),
    url(r'^about-us/$', AboutView.as_view(), name='about'),
    url(r'^partners/$', PartnersView.as_view(), name='partners'),
    url(r'^detail/(?P<pid>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^search-bar/$', search, name='search_bar'),
    url(r'^contact-form/$', ContactFormView.as_view(), name='contact_form'),


]
