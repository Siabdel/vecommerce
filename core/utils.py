# -*- coding:UTF-8 -*-
import os
import csv
import random
import logging
import pytz
import json
import io
import base64
import math
from dateutil.rrule import advance_iterator, rrule, DAILY # pip install dateutils
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext as _
from django.core import serializers
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
 
#from djqscsv import render_to_csv_response
from django.http import JsonResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import ensure_csrf_cookie


def render_json_response(queryset):
    """
    export json format
    """
    json_data = serializers.serialize('json', queryset)
    # Proceed to create your context object containing the columns and the data
    return HttpResponse(json_data, content_type='application/json')

def django_query_serializable(data):
    data_final = []
    new_class = data.first().__class__
    for item in data:
        itemID = str(item.object_id)
        # new_row = dict([(fld.name, getattr(item, fld.name))
        new_row = dict([(fld.name, item)
                        for fld in new_class._meta.fields if fld.name])
        data_final.append(new_row)

    return data_final

class Dict2Obj(object):
    """
    Turns a dictionary into a class
    result = {'code_of' : of.code_of, 'proposition' : proposition_2}
    return  models.Dict2Obj(result)
    """
    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

class JsonResponseMixin(object):
    """
    Return json
    """
    def render_to_json(self, queryset):
        # queryset  serialise
        data = serializers.serialize('json', queryset)

        json_data = json.loads( data)
        # json_data = json.dumps( data)

        # data_light = [ (elem['pk'], elem['fields']) for elem in json_data ]
        data_light = [ ]
        for elem in json_data:
            elem['fields']['pk'] = elem['pk']
            data_light.append(elem['fields'])

        data_fin = json.dumps(data_light)
        return HttpResponse(data_fin ,  content_type='application/json')

    def export_as_json(self, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    def export_as_cvs(self, queryset ):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        # response['Content-Disposition'] = 'attachment; filename="%s"'% os.path.join('export', 'export_of.csv')
        writer = csv.writer(response)
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
            ])
        return response
