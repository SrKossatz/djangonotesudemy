from contact.models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # importa o operador OR
from django.core.paginator import Paginator

from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['first_name', 'last_name', 'phone',]
    
    
  def clean(self):
    cleaned_data = self.cleaned_data
    self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid'))
    

def create(request):
  print(request.POST.get('first_name'))
  if request.method == 'POST':
    context = { 'form': ContactForm(request.POST) }
    return render(request, 'contact/create.html', context)  # retorna o formulário preenchido

  context = { 'form': ContactForm() } # retorna o formulário vazio

  return render(request, 'contact/create.html', context)  
