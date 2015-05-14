from django.views.generic import TemplateView
import random

class HomeView(TemplateView):

    template_name = 'index.html'

    def build_dict(self, list):
        ilist = [];
        for i in range(1, 1000):
            dict = {"item": i, "color": random.choice(list)}
            ilist.append(dict)
        return ilist


    def get_context_data(self, **kwargs):
        purple_list = ["#A183B6", "#E8DFEF", "#C7B3D6", "#7E5999", "#5D337B"]
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Brad Rice home"
        color_list =  ["#A183B6", "#E8DFEF", "#C7B3D6", "#7E5999", "#5D337B", "#DDF2AA", "#F7FCEB", "#ECF8CD", "#BBD776", "#8DAD41", "#FFF0B3", "#FFFCED", "#FFF7D3", "#E4D07E", "#B7A145"]
        context['p_list'] = self.build_dict(purple_list)
        context['c_list'] = self.build_dict(color_list)
        return context

