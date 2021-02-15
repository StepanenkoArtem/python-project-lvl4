"""Main view module."""
from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    """Generate simple main page."""
    output = {
        'test_text': _('This is a test page'),
    }
    return render(
        request,
        template_name='index.html',
        context=output,
    )
