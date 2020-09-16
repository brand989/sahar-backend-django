import os, sys
sys.path.insert(0, '/var/www/u1151312/data/www/sahar.dzygman.com/sale')
sys.path.insert(1, '/var/www/u1151312/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sale.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()