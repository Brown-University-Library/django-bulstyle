from django import template
from django.template.loader import get_template
from django.core.cache import cache
from django.utils.safestring import mark_safe
from .. import app_settings as settings
import requests

register = template.Library()
django_engine = template.engines['django']
BACKUP_HEADER_TEMPLATE = get_template(settings.header_local_backup())

def get_user_context(request):
    user = request.user
    if user.is_authenticated:
        return {
            'USER_NAME': user.email,
            'NEXT_URL': request.build_absolute_uri()
        }
    return {
        'NEXT_URL': request.build_absolute_uri()
    }

def get_config(request, non_auth_key, logged_in_key):
    if request.user.is_authenticated and logged_in_key:
        return logged_in_key
    return non_auth_key

def set_header_in_cache(cache_key, header):
    cache.set(
        cache_key,
        header,
        timeout=settings.header_cache_length()
    )

def get_header_from_cache(cache_key):
    return cache.get(cache_key)

def get_header_from_api(config_key):
    params = {'z': config_key}
    r = requests.get(settings.header_url(), params=params)
    if r.ok:
        return r.content.decode('utf8')
    return ""

def get_header_string(config_key):
    cache_key = f"bulheader:{config_key}"
    header = get_header_from_cache(cache_key)
    if not header:
        header = get_header_from_api(config_key)
        if header:
            set_header_in_cache(cache_key, header)
    return header

def get_header_template(config_key):
    template_string = get_header_string(config_key)
    if template_string:
        return django_engine.from_string(template_string)
    return BACKUP_HEADER_TEMPLATE

@register.simple_tag(takes_context=True)
def bul_header(context, bul_key=settings.header_subnav_key(), bul_login_key=settings.header_subnav_key()):
    request = context['request']
    config_string = get_config(request, bul_key, bul_login_key)
    bul_header_template = get_header_template(config_string)
    user_context = get_user_context(request)
    return mark_safe(
        bul_header_template.render(
            user_context
        )
    )
