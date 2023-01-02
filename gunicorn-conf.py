import os

port_number = int(os.environ.get('GUNICORN_PORT', 8000))
bind = '0.0.0.0:{0}'.format(port_number)

reload = True