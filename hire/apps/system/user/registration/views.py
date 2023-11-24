from django.views.generic               import TemplateView
from django.contrib.auth.mixins         import LoginRequiredMixin
from django.urls                        import reverse
from django.shortcuts                   import render, redirect
from django.contrib.auth                import login

from .forms                             import RegistrationForm
from ..                                 import template


class RegisterView(TemplateView):
    template_name = template.path('RegisterView')

    def get(self, request, *args, **kwargs):

        form = RegistrationForm()

        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user         = form.save()

            login(request, user)

            return redirect('/')

        return render(request, self.template_name, context={'form': form})


