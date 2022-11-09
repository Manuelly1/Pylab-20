from django import template

register = template.Library()

@register.filter(name="is_par")

def is_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False
