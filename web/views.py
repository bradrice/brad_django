from django.views.generic import TemplateView
import random
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class HomeView(TemplateView):

    template_name = 'index.html'

    def build_dict(self, list, num):
        ilist = [];
        for i in range(1, num):
            dict = {"item": i, "color": random.choice(list)}
            ilist.append(dict)
        return ilist


    def get_context_data(self, **kwargs):
        purple_list = ["#A183B6", "#E8DFEF", "#C7B3D6", "#7E5999", "#5D337B", "#ffffff"]
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Brad Rice home"
        color_list =  ["#A183B6", "#E8DFEF", "#C7B3D6", "#7E5999", "#5D337B", "#DDF2AA", "#F7FCEB", "#ECF8CD", "#BBD776", "#8DAD41", "#FFF0B3", "#FFFCED", "#FFF7D3", "#E4D07E", "#B7A145", "#ffffff"]
        context['p_list'] = self.build_dict(purple_list, 400)
        context['c_list'] = self.build_dict(color_list, 280)
        return context


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



