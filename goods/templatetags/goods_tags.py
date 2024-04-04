



from django import template
from goods.models import Catigories



register = template.Library()



@register.simple_tag()


def tag_catigories():
    return  Catigories.objects.all()
