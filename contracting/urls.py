from django.urls import path
from . import views
from . import forms

app_name = 'contracting'

urlpatterns = [
    path('contracting/quotes/',
         views.QuoteTaskStepListView.as_view(), name='quote_list'),
    path('contracting/create_quote/', forms.create_quote, name='create_quote'),
    path('contracting/edit_quote/<int:pk>/',
         forms.edit_quote, name='edit_quote'),
]
