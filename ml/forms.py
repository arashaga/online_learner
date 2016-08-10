# -*- coding: utf-8 -*-
from django import forms
from ml.validators import validate_file_extension
from .preprocess import preview_data
from .models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        validators=[validate_file_extension]

    )


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
    df = preview_data(path_to_file)
    columns = df.columns
    return zip(columns, columns)


