from django import template

register = template.Library()

@register.filter(name='slice_data')

def slice_data(list,slice_size):
    chunk = []
    i = 0
    for data in list:
        chunk.append(data)
        i = i+1
        if i == slice_size:
            yield chunk
            i = 0
            chunk = []
    yield chunk
    