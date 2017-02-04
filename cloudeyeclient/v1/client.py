#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
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

from cloudeyeclient.common import httpclient
from cloudeyeclient.v1 import alarm_mgr
from cloudeyeclient.v1 import metric_mgr
from cloudeyeclient.v1 import quota_mgr

LOGGER = logging.getLogger(__name__)


class Client(object):
    """Client for the HuaWei AutoScaling v1 API."""

    # service name registered in openstack
    service_name = 'cloudeye'

    def __init__(self, session=None, endpoint=None, **kwargs):
        """Initialize a new client for the VBS v2 API.

        :param keystoneauth1.session.Session session:
            The session to be used for making the HTTP API calls.  If None,
            a default keystoneauth1.session.Session will be created.
        :param string endpoint:
            An optional URL to be used as the base for API requests on this API
        :param kwargs:
            Keyword arguments passed to keystoneauth1.session.Session().
        """

        # http_log_debug = utils.get_effective_log_level() <= logging.DEBUG
        default_options = {
            'service_name': self.service_name,
            'client_name': 'Cloud Eye Client',
            'client_version': 'V1.0',
            'logger': LOGGER,
        }
        kwargs.update(default_options)

        if endpoint:
            endpoint += '/V1.0/%(project_id)s'
        self.client = httpclient.OpenStackHttpClient(session, endpoint, **kwargs)

        # initial manager of cloud eye
        self.metric_mgr = metric_mgr.MetricManager(self.client)
        self.alarm_mgr = alarm_mgr.AlarmManager(self.client)
        self.quota_mgr = quota_mgr.QuotaManager(self.client)

