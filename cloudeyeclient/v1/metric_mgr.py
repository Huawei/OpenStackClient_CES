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

from cloudeyeclient.common import manager
from cloudeyeclient.common import utils
from cloudeyeclient.v1 import resource


class MetricManager(manager.Manager):
    """Cloud Eye metric API management"""

    resource_class = resource.Metric

    def list(self, namespace=None, metric_name=None, dim=None, start=None,
             limit=None, order=None):
        params = utils.remove_empty_from_dict({
            "namespace": namespace,
            "metric_name": metric_name,
            "start": start,
            "dim": None,
            "limit": limit,
            "order": order
        })
        return self._list('/metrics', key='metrics', params=params)
