from django. forms import ModelForm
from django import forms
from .models import Qurilish
from django.forms.models import inlineformset_factory


# class QurilishForm(ModelForm):
#     class Meta:
#         model = Qurilish
#         fields = ['q_type', 'servise_name', 'servise_code', 'soato', 'report_month', 'report_year', 'last_year']
#
#
#


class CollectionTitleForm(forms.ModelForm):

    class Meta:
        model = Qurilish
        exclude = ()

CollectionTitleFormSet = inlineformset_factory(
   Qurilish, form=CollectionTitleForm,
    fields=['q_type', 'servise_name', 'servise_code', 'soato', 'report_month', 'report_year', 'last_year', ], extra=1, can_delete=True
)