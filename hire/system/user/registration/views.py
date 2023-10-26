from django.views.generic               import TemplateView
from django.contrib.auth.mixins         import LoginRequiredMixin
from django.shortcuts                   import render

from ..                                 import template


class RegisterView(LoginRequiredMixin, TemplateView):
    template_name = template.path('RegisterView')

    def get(self, request, *args, **kwargs):

        version = '2'

        return render(request, self.template_name, context={'version': version})

