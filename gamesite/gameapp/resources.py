from import_export import resources
from .models import *

class GameResource(resources.ModelResource):
    class meta:
        model = Game