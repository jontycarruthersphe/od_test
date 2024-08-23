__import__("pkg_resources").declare_namespace(__name__)

from .version import __version__
from .od_matrix import OriginDestination

__all__ = ['OriginDestination']

