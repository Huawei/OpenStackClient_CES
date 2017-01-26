#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import logging

from osc_lib import utils

from cloudeyeclient.common.parser_builder import BaseParser

LOGGER = logging.getLogger(__name__)

# client-manage[API_NAME]
API_NAME = 'cloudeye'
# Fixed Name
DEFAULT_API_VERSION = '1.0'
# default.json->vbs_api_version
API_VERSION_OPTION = 'os_cloudeye_api_version'
API_VERSIONS = {
    '1.0': 'cloudeyeclient.v1.client.Client',
}


def make_client(instance):
    """Returns an orchestration service client"""

    api_version = instance._api_version[API_NAME]
    as_client_clazz = utils.get_client_class(API_NAME, api_version, API_VERSIONS)

    kwargs = {
        'region_name': instance.region_name,
        'interface': instance.interface
    }
    endpoint = instance._cli_options.config.get('cloudeye_endpoint_override', None)

    LOGGER.debug('Instantiating cloud eye client: %s', as_client_clazz)
    LOGGER.debug('Instantiating cloud eye client with kwargs: %s', kwargs)
    LOGGER.debug('Instantiating cloud eye client with endpoint: %s', endpoint)
    client = as_client_clazz(instance.session, endpoint, **kwargs)
    return client


def build_option_parser(parser):
    """Hook to add global options"""
    BaseParser.register_service_option(parser, API_NAME)
    return parser
