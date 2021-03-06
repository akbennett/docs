"""Open Source Foundries Sphinx extensions"""

from rpi3 import OsfRPi3LinksDirective


def setup(app):
    app.add_config_value('osf_subscriber_version', None, 'env')
    '''Latest released version for subscribers'''

    app.add_config_value('osf_public_version', None, 'env')
    '''Latest released version to the public'''

    app.add_directive('osf-rpi3-links', OsfRPi3LinksDirective)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
