from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page
    """
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})
"""
class PageDetailView(DetailView):
    model = Page

# Lo he aniadido para la leccion 19: vistas CRUD
class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']
    # Se envia a la lista principal:
    success_url = reverse_lazy('pages:pages')


# Lo he aniadidod para la leccion 20:
class PageUpdate(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args= [self.object.id]) + '?ok'


class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')