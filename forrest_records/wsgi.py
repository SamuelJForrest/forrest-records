"""
WSGI config for forrest_records project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/root/projects/forrest_records/forrest-records')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forrest_records.settings')

application = get_wsgi_application()
