from django import template

register = template.Library()

@register.filter
def get_by_index1(mylist, index):
    return mylist[index][1]

@register.filter
def get_by_index(mylist, index):
    return mylist[index]
