from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    
    template_name = "core/home.html"

    """ Esto hace lo mismo que get()
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Mi super web Playground"
            return context
    """
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, {'title':"Mi SUPER web Playground"})

class SamplePageView(TemplateView):
    
    template_name = "core/sample.html"
