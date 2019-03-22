from django import forms
from django.forms import formset_factory
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from crispy_forms.layout import Submit
from .custom_layout_object import *

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ParentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'card bg-primary'
        self.helper.label_class = 'form'
        self.helper.field_class = 'col-md-9 mx-1 card-body'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('pics'),
                Field('address'),
                )
            )


ParentFormSet = inlineformset_factory(
    Student, Parent, form=ParentForm,
    fields=['name', 'pics', 'address'], can_delete=False
)

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ['owned_by', ]

BookFormSet = inlineformset_factory(
    Student, Book, form=BookForm,
    fields=['name', 'ISBN', 'purpose'], 
    extra=1,
    can_delete=True
)

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('pics'),
                Field('address'),
                Field('city'),
                Field('local_government_origin'),
                Field('local_government_residence'),
                Field('state_origin'),
                Field('state_residence'),
                Field('date_of_birth'),
                HTML("<br>"),
                Fieldset('Add books',
                    Formset('book')),
                HTML("<br>"),
                Fieldset('Add Parent',
                    Formset('parent')),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )
class LiteracyForm(forms.ModelForm):

    class Meta:
        model = Literacy
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(LiteracyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.form_method = 'post'
        self.helper.field_class = 'col-md-9'
        self.helper.form_action = 'student_literacy_create'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('literacy'),
                Field('describe_literacy'),
            ))
        self.helper.add_input(Submit('submit', 'Submit'))
        
LiteracyFormSet = formset_factory(Literacy)

class NumeracyForm(forms.ModelForm):

    class Meta:
        model = Numeracy
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('numeracy'),
                Field('numeracy_literacy'),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('date'),
                Field('present'),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )

class IncentiveForm(forms.ModelForm):

    class Meta:
        model = Incentive
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('description_of_incentive'),
                Field('date_of_inclusion'),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )
        
class AppraisalForm(forms.ModelForm):

    class Meta:
        model = Appraisal
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('method_of_appraisal'),
                Field('performance'),
                Field('brief'),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )

class PostingForm(forms.ModelForm):

    class Meta:
        model = Appraisal
        exclude = ['student', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('method_of_appraisal'),
                Field('performance'),
                Field('brief'),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )