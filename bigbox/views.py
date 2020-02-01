################################################################################
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from django.core.paginator import Paginator
from .models import Activity,Box,Category,CommonInfo
################################################################################

# Create your views here.

################################################################################
class BoxObjectMixin(object):
    model = Box
    lookup = 'id'

    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        return get_object_or_404(Box, id=lookup)
################################################################################

################################################################################
class BoxListView(ListView):
    model = Box
    template_name = 'bigbox/box.html' #<app>/<model>_<viewtype>.html
    #Esto es lo que va a aparecer en nuestro template
    context_object_name = 'boxes'
    #Para que aparescan del mas nuevo al mas viejo
    #ordering = ['internal_name']

################################################################################

################################################################################
class BoxDetailView(DetailView, BoxObjectMixin):
    model = Box
    template_name = 'bigbox/box_detail.html'

    def get_object(self):
        #self.kwargs se utiliza para acceder a parametros en class based views
        id = self.kwargs.get("id")
        return get_object_or_404(Box, id=id)
################################################################################

################################################################################
class ActivityListView(ListView, BoxObjectMixin):
    model = Activity
    template_name = 'bigbox/activity_list.html'
    #ordering = ['name']
    paginate_by = 20

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['lola'] = self.get_object()
        return context
################################################################################

################################################################################
class ActivityDetailView(DetailView):
    model = Activity
################################################################################
