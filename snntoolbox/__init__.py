# coding=utf-8

"""
Import common functions and initialize working directory.
"""

from __future__ import absolute_import, print_function

import os

from snntoolbox.config import update_setup
from snntoolbox.core.pipeline import test_full
from snntoolbox.core.util import get_range


# Set a base directory for the toolbox.
_base_dir = os.path.expanduser('~')
if not os.access(_base_dir, os.W_OK):
    _base_dir = '/tmp'

# Toolbox root directory.
toolbox_root = os.path.join(_base_dir, '.snntoolbox')
if not os.path.exists(toolbox_root):
    os.makedirs(toolbox_root)

# Path to toolbox preferences.
_config_path = os.path.join(toolbox_root, 'preferences')
if not os.path.exists(_config_path):
    os.makedirs(_config_path)

# python 2 can not handle the 'flush' keyword argument of python 3 print().
# Provide 'echo' function as an alias for
# "print with flush and without newline".
try:
    from functools import partial
    echo = partial(print, end='', flush=True)
    echo(u'')
except TypeError:
    # TypeError: 'flush' is an invalid keyword argument for this function
    import sys

    def echo(text):
        """python 2 version of print(end='', flush=True)."""
        sys.stdout.write(u'{0}'.format(text))
        sys.stdout.flush()
