from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView
                                  ,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

class CBView(View):
    def get(self,request):
        return HttpResponse("class base views are so cool!!!")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index_inject'] = 'Basic INJECTION!'
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'StudentDetails/school_details.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("myApp:school_list")