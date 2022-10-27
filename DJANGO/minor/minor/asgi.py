"""
ASGI config for minor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
>>>>>>> 86824304de2580eeee05b3472a6bea444bc535d1
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minor.settings')

application = get_asgi_application()
