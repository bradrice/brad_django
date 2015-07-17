from django.views.generic import TemplateView
import random
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class HomeView(TemplateView):

    template_name = 'index.html'


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/contact/'

    def dispatch(self, *args, **kwargs):
        return super(ContactCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('resume'))



