from django import template

register = template.Library()


@register.filter
def mergelistclient(items):
    email_client = [item.email for item in items]
    return ', '.join(email_client)
