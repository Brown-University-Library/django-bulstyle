# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from ..app_settings import container_class

register = template.Library()

@register.assignment_tag
def bulstyle_container():
    """
    **Tag name**::
        bulstyle_container
    Returns the container class for the appliction
    Default value: ``container``
    Alternatively the value is ``container-fluid``
    This value is configurable, see Settings section
    **Usage**::
        {% bulstyle_container %}
    **Example**::
        {% bulstyle_container %}
    """
    return container_class()
