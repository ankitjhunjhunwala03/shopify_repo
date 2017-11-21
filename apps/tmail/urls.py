from django.conf.urls import url
from .views import trigger_email
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^send_mail/', csrf_exempt(trigger_email), name='trigger_email'),
]
