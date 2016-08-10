# -*- coding: utf-8 -*-
from django import forms
from ml.validators import validate_file_extension
from .preprocess import import_data
from .models import Document
from django.core import validators
from django.core.exceptions import ValidationError

###############
class CommaSepratedField(forms.Field):


    def __init__(self, base_field=None, separator=",", *args, **kwargs):
        super(CommaSepratedField, self).__init__(*args, **kwargs)
        self.base_field = base_field
        self.separator = separator

    def clean(self, data):
        if not data:
            raise forms.ValidationError('Enter at least one value.')
        self.value_list = data.split(self.separator)
        if self.base_field is not None:
            base_field = self.base_field()
            for value in self.value_list:
                base_field.clean(value)
        return data

    def get_list(self):
        return self.value_list

###########

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        validators=[validate_file_extension]

    )
    headers = CommaSepratedField()


class FeatureSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FeatureSelectForm, self).__init__(*args, **kwargs)
        self.fields['choices'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=get_my_choices())





class TargetSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TargetSelectForm, self).__init__(*args, **kwargs)
        self.fields['target'] = forms.ChoiceField(widget=forms.RadioSelect,
                                             choices=get_my_choices())


####Utililty function

def get_my_choices():
    path_to_file = str(Document.objects.last().docfile)
    df = import_data(path_to_file)
    columns = df.columns
    return zip(columns, columns)



