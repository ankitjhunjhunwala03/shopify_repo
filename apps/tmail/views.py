# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.http.response import JsonResponse

# Create your views here.


def get_value_from_dict(key, dictionary):
    if key not in dictionary.keys():
        raise ValueError('Key: "%s" not found' % key)
    return dictionary[key]


def trigger_email(request):
    data = request.POST
    try:
        to_email = get_value_from_dict('to_email', data)
        from_email = get_value_from_dict('from_email', data)
        subject = get_value_from_dict('subject', data)
        body = get_value_from_dict('body', data)
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    try:
        send_mail(subject, body, from_email, [to_email], fail_silently=False)
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    return JsonResponse({'status': '1'})
