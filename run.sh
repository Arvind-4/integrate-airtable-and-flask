#!/bin/bash

set -e
gunicorn -c gunicorn-conf.py app.main:app