from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import zipfile

from ml.models import Document
from ml.forms import DocumentForm, FeatureSelectForm, TargetSelectForm
from ml.preprocess import import_data
import os



def home(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])

            debug_msg = request.POST['headers']
            newdoc.save()

            feature_form = FeatureSelectForm(request.POST)
            target_form = TargetSelectForm(request.POST)
            ## TODO: Fixes(view)you need to make a eparate view for the below forms to validate them
            ##TODO: 5- implement the file storage system
            ##TODO:     5.1-implement the S# bucket maybe
            ##TODO:     5.2-implement the zip archiving and extracting like below

            ##This is to implement zip archiving



            #filename, file_extension = os.path.splitext(tail)
            # you can use newdoc.path to get the file path#
            # zf = zipfile.ZipFile(head+filename +'.zip', mode='w')
            # try:
            #     zf.write(filename +'.zip')
            # finally:
            #     zf.close()
            #####################################################
            df = import_data(newdoc.docfile) # i sue this approach to avoid hitting database
            html = df.to_html(max_rows=3)
            return render_to_response(
                'preprocessing.html',
                {'filename': request.FILES['docfile'],
                 'shape': df.shape,
                 'data_preview' : html,
                 'feature_form' : feature_form,
                 'target_form'  : target_form,
                 'file_id'  : newdoc.id,

                 'debug_msg' : debug_msg,
                 },
                context_instance=RequestContext(request)
            )
        else:
            validator_msg = 'File is not supported'
            return render_to_response(
                'index.html',
                {'form': form, 'validator_msg': validator_msg},
                context_instance=RequestContext(request)
            )

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('ml.views.list'))
    else:
        form = DocumentForm()
        return render_to_response(
            'index.html',
            {'form': form},
            context_instance=RequestContext(request)
        )
        # A empty, unbound form

    # Render list page with the documents and the form

    # return render(request, 'index.html',
    #               {
    #                   'document' : documents,
    #                   'form' : form
    #               },
    #               content_type='application/xhtml+xml')

def preprocessing(request,file_id):

    if request.method == 'POST':
        file_id = get_object_or_404(Document, pk=file_id)
        #filename = Document.objects.filter(id=file_id)
        target = request.POST['target']

        ## this is to get a list of selected values from the multiple checkbox
        features = request.POST.getlist('choices')
        return render(request, 'pre-confirm.html', {#'filename': filename,
                                                      'file_id': file_id,
                                                      'target': target,
                                                      'features': features})

def train_using_regression(request, file_id):
    file_id = get_object_or_404(Document, pk=file_id)

    filename = file_id.docfile
    df = import_data(filename)
    target = request.POST['target']
    features = request.POST.getlist('choices')
    from sklearn.cross_validation import train_test_split

    X, y = df.iloc[:, 1:].values, df.iloc[:, 0].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    ## add normalization here page 111

    from sklearn.linear_model import LinearRegression
    slr = LinearRegression()
    slr.fit(X_train, y_train)
    return render(request, 'pre-confirm.html', {  # 'filename': filename,
        'file_id': file_id,
        'target': target,
        'features': features,
        'coefs' : slr.coef_,
        'arash' : "Arash",})