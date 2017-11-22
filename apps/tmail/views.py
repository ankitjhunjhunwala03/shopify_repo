# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.


def get_value_from_dict(key, dictionary):
    if key not in dictionary.keys():
        raise ValueError('Key: "%s" not found' % key)
    return dictionary[key]


def trigger_email(request):
    data = request.POST
    try:
        bcc = None
        context = {}
        to_email = get_value_from_dict('to_email', data)
        to_email = to_email.split(',')
        from_email = get_value_from_dict('from_email', data)
        subject = get_value_from_dict('subject', data)
        body = get_value_from_dict('body', data)
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    try:
        msg = EmailMultiAlternatives(
            subject, body, from_email, to_email, bcc)
        msg.encoding = "utf-8"
        msg.content_subtype = "html"
        try:
            html_content = render_to_string(body, context)
            msg.attach_alternative(html_content, "text/html")
        except Exception, e:
            print str(e)
        msg.send()
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    return JsonResponse({'status': '1'})
