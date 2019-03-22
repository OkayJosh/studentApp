from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.db import transaction
from django.http import HttpResponse
# Create your views here.


class HomepageView(TemplateView):
    template_name = "student/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.order_by('id')
        return context


##########################################################################
#                          Student views                             #
##########################################################################

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context


class StudentCreate(CreateView):
    model = Student
    template_name = 'student/student_create.html'
    form_class = StudentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(StudentCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['book'] = BookFormSet(self.request.POST)
            data['parent'] = ParentFormSet(self.request.POST)
        else:
            data['book'] = BookFormSet()
            data['parent'] = ParentFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        book = context['book']
        parent = context['parent']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if book.is_valid():
                book.instance = self.object
                book.save()
            if parent.is_valid():
                parent.instance = self.object
                parent.save()
        return super(StudentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student:student_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_create.html'

    def get_context_data(self, **kwargs):
        data = super(StudentUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['book'] = BookFormSet(self.request.POST, instance=self.object)
            data['parent'] = ParentFormSet(self.request.POST, instance=self.object)
        else:
            data['book'] = BookFormSet(instance=self.object)
            data['parent'] = ParentFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        book = context['book']
        parent = context['parent']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if book.is_valid():
                book.instance = self.object
                book.save()
            if parent.is_valid():
                parent.instance = self.object
                parent.save()
        return super(StudentUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student:student_detail', kwargs={'pk': self.object.pk})


class StudentDelete(DeleteView):
    model = Student
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('student:homepage')

##########################################################################
#                         Literacy views                             #
##########################################################################


class LiteracyBaseView(TemplateView):
    template_name = "student/student_literacy_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['literacys'] = Literacy.objects.order_by('id')
        return context

class LiteracyDetailView(DetailView):
    model = Literacy
    template_name = 'student/student_literacy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LiteracyDetailView, self).get_context_data(**kwargs)
        return context


class LiteracyCreateView(CreateView):
    model = Literacy
    template_name = 'student/student_literacy_create.html'
    form_class = LiteracyForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(LiteracyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['literacy'] = LiteracyFormSet(self.request.POST)
        else:
            data['literacy'] = LiteracyFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        literacy = context['literacy']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if literacy.is_valid():
                literacy.instance = self.object
                literacy.save()

        return super(LiteracyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student:student_literacy_detail', kwargs={'pk': self.object.pk})