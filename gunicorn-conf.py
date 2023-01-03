import os

port_number = int(os.environ.get("GUNICORN_PORT", 8000))
bind = f"0.0.0.0:{port_number}"

reload = True
