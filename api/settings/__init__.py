from api.settings.base import *

try:
    from api.settings.local import *
except ImportError, e:
    raise ImportError("Failed to import local settings")
