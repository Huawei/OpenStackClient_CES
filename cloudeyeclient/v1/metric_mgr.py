#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import time
from cloudeyeclient.common import manager
from cloudeyeclient.common import utils
from cloudeyeclient.v1 import resource


class MetricManager(manager.Manager):
    """Cloud Eye metric API management"""

    resource_class = resource.Metric

    def list(self, namespace=None, metric_name=None, dimensions=[], start=None,
             limit=None, order=None):
        """list metric

        :param namespace:
        :param metric_name:
        :param dimensions: ["${key},${value}", ..]
        :param start: "${key}:${value}"
        :param limit:
        :param order:
        :return:
        """
        params = utils.remove_empty_from_dict({
            "namespace": namespace,
            "metric_name": metric_name,
            "start": start,
            "limit": limit,
            "order": order
        })
        if dimensions:
            for (idx, dimension) in enumerate(dimensions):
                params["dim.%d" % idx] = dimension
        return self._list('/metrics', key='metrics', params=params)

    def list_favorite(self):
        """list favorite metric"""
        return self._list('/favorite-metrics', key='metrics')

    def list_metric_data(self, namespace, metric_name, from_, to, period,
                         filter_, dimensions):
        """list metric data"""
        params = {
            "namespace": namespace,
            "metric_name": metric_name,
            "from": utils.get_milliseconds(from_),
            "to": utils.get_milliseconds(to),
            "period": period,
            "filter": filter_,
        }

        for (idx, dimension) in enumerate(dimensions):
            params["dim.%d" % idx] = dimension
        return self._list('/metric-data',
                          params=params,
                          key='datapoints',
                          resource_class=resource.MetricData)

    def add_metric_data(self, namespace, metric_name, dimensions, ttl,
                        collect_time, value, unit=None, type_=None):
        """add metric data"""
        data = utils.remove_empty_from_dict({
            "metric": {
                "namespace": namespace,
                "dimensions": dimensions,
                "metric_name": metric_name
            },
            "ttl": ttl,
            "collect_time": utils.get_milliseconds(collect_time),
            "value": value,
            "unit": unit,
            "type": type_
        })

        return self._create('/metric-data', json=[data], raw=True)
