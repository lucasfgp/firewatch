import datetime
from django import template
from firedata.models import BurningEvent

register = template.Library()

@register.simple_tag
def get_fire_events_count():
    return BurningEvent.objects.all().count()

@register.simple_tag
def get_todays_date():
    return datetime.datetime.now().strftime("%d %b, %Y")