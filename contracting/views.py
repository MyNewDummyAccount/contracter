from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Quote, Task, Step


class QuoteTaskStepListView(ListView):
    model = Quote
    template_name = 'quote_task_step_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(quote=self.object)
        context['steps'] = Step.objects.filter(task__in=context['tasks'])
        return context
