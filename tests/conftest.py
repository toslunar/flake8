import sys

import flake8

flake8.configure_logging(2, 'test-logs-%s.%s.log' % sys.version_info[0:2])
