# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

BULSTYLE_DEFAULTS = {
        'container_class': 'container',
        'header_url': 'https://library.brown.edu/common/includes/bul_pl_header.php',
        'header_cache_length': 500,
        'header_subnav_key': '',
        'header_subnav_login_key': '',
        'header_local_backup': 'bulstyle/BUL_HEADER_BACKUP.html',
        'footer_url': 'https://library.brown.edu/common/includes/bul_pl_footer.php',
        'footer_cache_length': 5000,
        'footer_local_backup': 'bulstyle/BUL_FOOTER_BACKUP.html',
}

BULSTYLE = BULSTYLE_DEFAULTS.copy()
# Override with user settings from settings.py
BULSTYLE.update(getattr(settings, 'BULSTYLE', {}))

def get_bulstyle_setting(setting, default=None):
    """
    Read a setting
    """
    return BULSTYLE.get(setting, default)

def container_class():
    return get_bulstyle_setting('container_class')

def header_url():
    return get_bulstyle_setting('header_url')

def header_cache_length():
    return get_bulstyle_setting('header_cache_length')

def header_subnav_key():
    return get_bulstyle_setting('header_subnav_key')

def header_subnav_login_key():
    return get_bulstyle_setting('header_subnav_login_key') or header_subnav_key()

def header_local_backup():
    return get_bulstyle_setting('header_local_backup')

def footer_url():
    return get_bulstyle_setting('footer_url')

def footer_cache_length():
    return get_bulstyle_setting('footer_cache_length')

def footer_local_backup():
    return get_bulstyle_setting('footer_local_backup')
