from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from tickets.models import Tech
from tickets.form import TechForm

from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login')
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class': 'form-control'})

        return form
    
class ProfileUpdateView(UpdateView):
    form_class = TechForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile.html'

    def get_object(self):
        profile, created = Tech.objects.get_or_create(user = self.request.user)
        return profile
    

