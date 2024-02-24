from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spam"] = [f"egg_{i}" for i in range(10)]
        return context
