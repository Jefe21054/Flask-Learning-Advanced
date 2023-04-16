import os

from app import create_app

settings_module = os.getenv('CONFIG_ENV')

app = create_app(settings_module)
