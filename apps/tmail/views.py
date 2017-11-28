# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http.response import JsonResponse
from django.template import Template, Context
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from tmail.models import EmailTemplate

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
        subject = data.get('subject')
        template_id = data.get('template_id')
        body = data.get('body')
        context = json.loads(data.get('context', "{}"))
        if template_id:
            template = EmailTemplate.objects.get(id=template_id)
            subject = template.subject
            body = template.body

        t = Template(subject)
        c = Context(context)
        subject = t.render(c)
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    try:
        msg = EmailMultiAlternatives(
            subject, body, from_email, to_email, bcc)
        msg.encoding = "utf-8"
        msg.content_subtype = "html"
        try:
            t = Template(body)
            c = Context(context)
            html_content = t.render(c)
            msg.attach_alternative(html_content, "text/html")
        except Exception, e:
            print str(e)
        msg.send()
    except Exception, e:
        return JsonResponse({'status': '0', 'error': str(e)})
    return JsonResponse({'status': '1'})
