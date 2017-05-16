# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

BULSTYLE_DEFAULTS = {
        'container_class': 'container',
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

