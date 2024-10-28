from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from tickets.form import TicketForm
from .models import Ticket, Tech

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'tickets/base.html')

@method_decorator(login_required, name='dispatch')
class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/tickets_list.html'
    context_object_name = 'tickets'

    # def get_queryset(self):
    #     return Ticket.objects.filter(tech= Tech.objects.get(user=self.request.user))
    
@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'tickets/tickets_create.html'
    # fields = ['title', 'description']
    form_class = TicketForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        tech_intance = Tech.objects.get(user=self.request.user)
        form.instance.tech = tech_intance
        self.object = form.save()
        response = super().form_valid(form)
        return response  

@method_decorator(login_required, name='dispatch')
class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/tickets_details.html'
    context_object_name = 'ticket'

@method_decorator(login_required, name='dispatch')
class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/tickets_delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'ticket'

    def get_object(self, queryset=None):
        ticket = super().get_object(queryset)

        if ticket.tech == Tech.objects.get(user=self.request.user):
            return ticket
        else:
            raise Http404('No tienes los permisos suficientes para ELIMINAR este ticket...')

@method_decorator(login_required, name='dispatch')
class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = 'tickets/tickets_update.html'
    # fields = ['title', 'description']
    form_class = TicketForm
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
        ticket = super().get_object(queryset)

        if ticket.tech == Tech.objects.get(user=self.request.user):
            return ticket
        else:
            raise Http404('No tienes los permisos suficientes para ACTUALIZAR este ticket...')

