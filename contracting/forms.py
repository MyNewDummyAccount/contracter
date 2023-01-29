from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import inlineformset_factory
from .models import Quote, Task, Step


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['date_requested', 'date_delivered', 'total_cost', 'details']


TaskFormSet = inlineformset_factory(Quote, Task, fields=(
    'name', 'details'), extra=1, can_delete=True)
StepFormSet = inlineformset_factory(Task, Step, fields=(
    'name', 'time_estimate', 'material_description', 'material_estimate', 'details'), extra=1, can_delete=True)


def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        task_formset = TaskFormSet(request.POST, prefix='tasks')
        if form.is_valid() and task_formset.is_valid():
            quote = form.save()
            tasks = task_formset.save(commit=False)
            for task in tasks:
                task.quote = quote
                task.save()
            return redirect('contracting/quotes')
    else:
        form = QuoteForm()
        task_formset = TaskFormSet(prefix='tasks')
    return render(request, 'contracting/create_quote.html', {'form': form, 'task_formset': task_formset})


def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        task_formset = TaskFormSet(
            request.POST, instance=quote, prefix='tasks')
        step_formset = StepFormSet(
            request.POST, instance=quote, prefix='steps')
        if form.is_valid() and task_formset.is_valid() and step_formset.is_valid():
            quote = form.save()
            tasks = task_formset.save(commit=False)
            steps = step_formset.save(commit=False)
            for task in tasks:
                task.quote = quote
                task.save()
            for step in steps:
                step.task = task
                step.save()
            return redirect('contracting/quotes')
    else:
        form = QuoteForm(instance=quote)
        task_formset = TaskFormSet(instance=quote, prefix='tasks')
        step_formset = StepFormSet(instance=quote, prefix='steps')
    return render(request, 'contracting/edit_quote.html', {'form': form, 'task_formset': task_formset, 'step_formset': step_formset})
