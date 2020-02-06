################################################################################
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from django.core.paginator import Paginator
from .models import Activity,Box,Category,CommonInfo
################################################################################

# Create your views here.

################################################################################
class BoxListView(ListView):
    model = Box
    template_name = 'bigbox/box.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'boxes'
################################################################################

################################################################################
class BoxDetailView(DetailView):
    model = Box
    template_name = 'bigbox/box_detail.html'

    def get_object(self):
        """
        Tomo el id del Box correspondiente al del detalle
        """
        id = self.kwargs.get("id")
        return get_object_or_404(Box, id=id)
################################################################################

################################################################################
class ActivityListView(DetailView):
    model = Box
    template_name = 'bigbox/activity_list.html'

    def get_context_data(self, **kwargs):
        """
        En esta funcion defino un contexto con las activities
        del objeto tomado y luego realizo su paginacion.
        """
        context = super(ActivityListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        activities = Paginator(self.object.activities.all(), 20)
        context['activities'] = activities.get_page(page)
        context['activities_number'] = self.object.activities.count()
        return context

    def get_object(self):
        """
        Tomo el id del Box correspondiente al del detalle
        """
        #self.kwargs se utiliza para acceder a parametros en class based views
        id = self.kwargs.get("id")
        return get_object_or_404(Box, id=id)
################################################################################

################################################################################
class ActivityDetailView(DetailView):
    model = Activity
################################################################################
