from django import template

register = template.Library()

@register.filter(name='sacar')
def sacar (value, args):
    return value.__getattribute__(args)

@register.filter(name='adicionar')
def adicionar (value, args):
    return value+args