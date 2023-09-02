from django import template

register = template.Library()


@register.filter
def mergelistclient(items):
    email_client = [item.email for item in items]
    return ', '.join(email_client)


@register.filter
def mergelistserverresponse(items):
    email_client = [f'{item.get_status_display()}: {item.server_response}' for item in items]
    return '\n'.join(email_client)
