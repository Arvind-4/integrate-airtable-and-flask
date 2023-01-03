"""Dotenv Module"""
from decouple import config

BASE_URL = "https://api.airtable.com"

VERSION = "v0"

APPEND_SLASH = False

DEBUG = config("FLASK_DEBUG", cast=bool)
SECRET_KEY = config("FLASK_SECRET_KEY")

AIRTABLE_BASE_ID = config("AIRTABLE_BASE_ID", cast=str)
AIRTABLE_API_KEY = config("AIRTABLE_API_KEY", cast=str)
AIRTABLE_TABLE_NAME = config("AIRTABLE_TABLE_NAME", cast=str)
