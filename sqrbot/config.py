"""Configuration collection.
"""

__all__ = ('create_config',)

import os


def create_config():
    """Create a config mapping from defaults and environment variable
    overrides.

    Returns
    -------
    c : `dict`
        A configuration dictionary.

    Examples
    --------
    Apply the configuration to the aiohttp.web application::

        app = web.Application()
        app.update(create_config)
    """
    c = {}

    # Application run profile. 'development' or 'production'
    c['api.lsst.codes/profile'] = os.getenv(
        'API_LSST_CODES_PROFILE',
        'development').lower()

    # That name of the api.lsst.codes service, which is also the root path
    # that the app's API is served from.
    c['api.lsst.codes/name'] = os.getenv('API_LSST_CODES_NAME', 'sqrbot-jr')

    # The name of the logger, which should also be the name of the Python
    # package.
    c['api.lsst.codes/loggerName'] = os.getenv(
        'API_LSST_CODES_LOGGER_NAME', 'sqrbot')

    # Log level (INFO or DEBUG)
    c['api.lsst.codes/logLevel'] = os.getenv(
        'API_LSST_CODES_LOG_LEVEL',
        'info' if c['api.lsst.codes/profile'] == 'production' else 'debug'
    ).upper()

    return c