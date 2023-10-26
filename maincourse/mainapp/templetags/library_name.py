import datetime
from django import template

register = template.Library()

@register.filter(name="splitl")
def  splitl_func(value: str): # Из Hello_World получаеми Hello World
    return value.replace("_", " ")

def splitlvl_func(value: str, rplv: str):
    return value.replace(rplv, " ")

register.filter("split_vl", splitlvl_func)

@register.simple_tag(name="current_time")
def current_time(format_string):
    return "Текущее время" + str(datetime.datetime.now().strtime(format_string))

def now_time():
    return datetime.now()

register.simple_tag(now_time, name="now")

@register.simple_tag(takes_context=True, name="digit_square")
def square_value(context):
    return context['digit']**2

@register.inclusion_tag("red.html", name="red")
def red_text(text):
    return {'text': text}

@register.inclusion_tag("colored.html", takes_context=True, name="make_color")
def clr_text(context, text):
    return {'text': text, 'color': context['color']}