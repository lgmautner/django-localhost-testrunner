# -*- coding: utf-8 -*-

import djangotestrunner
from .version import __version__
from .runner import LocalhostTestRunner

__all__ = ('__version__', 'LocalhostTestRunner', 'djangotestrunner')
