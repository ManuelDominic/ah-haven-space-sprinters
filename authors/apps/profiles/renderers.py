import json

from authors.apps.authentication.default_renderer import BaseRenderer

class UserProfileJSONRenderer(BaseRenderer):
    data = 'profile'

