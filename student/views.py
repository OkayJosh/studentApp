from django.shortcuts import render
from django.urls import reverse_lazy
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
        context['Students'] = Student.objects.order_by('id')
        return context


##########################################################################
#                           Collection views                             #
##########################################################################

class StudentDetailView(DetailView):
    model = Collection
    template_name = 'student/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context


class StudentCreate(CreateView):
    model = Collection
    template_name = 'student/collection_create.html'
    form_class = StudentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['parent'] = ParentFormSet(self.request.POST)
            data['book'] = BookFormSet(self.request.POST)
        else:
            data['parent'] = ParentFormSet(self.request.POST)
            data['book'] = BookFormSet(self.request.POST)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        parent = context['parent']
        book = context['book']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if parent.is_valid():
                parent.instance = self.object
                parent.save()
            if book.is_valid():
                book.instance = self.object
                book.save()
        return super(StudentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student:student_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class CollectionUpdate(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'mycollections/collection_create.html'

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST, instance=self.object)
        else:
            data['titles'] = CollectionTitleFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:collection_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CollectionDelete(DeleteView):
    model = Collection
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('mycollections:homepage')