# -*- coding: utf-8 -*-

import localhostrunner
import os.path
from django.conf import settings
from django.test.runner import DiscoverRunner


class LocalhostTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        return localhostrunner.LocalhostTestRunner(**kwargs).run(suite)
