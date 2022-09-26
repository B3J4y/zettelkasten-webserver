from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Overview(TemplateView):
    """ Creates a page as an overview """
    template_name = 'kasten/overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """Get the overview page's template and context data"""
        context = self.get_context_data()
        return render(request, self.template_name, context)


class AddDirectory(TemplateView):
    """ Adding a page to add a directory of the Zettelkasten """
    template_name = 'kasten/directory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """Get the overview page's template and context data"""
        context = self.get_context_data()
        return render(request, self.template_name, context)
