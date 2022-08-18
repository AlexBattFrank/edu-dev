from django import template

register = template.Library()


bad_words = ['radish']


@register.filter(name='censor')
def censor(value):
    x = value.lower()
    if ' ' in x:
        a = list(x.split(' '))
        for i in a:
            if i in bad_words:
                y = a.index(i)
                a.remove(i)
                a.insert(y, 'r****h')
                value = (" ".join(a))
                return value

    if x in bad_words:
        x = 'r****h'
        return x
    else:
        return x
