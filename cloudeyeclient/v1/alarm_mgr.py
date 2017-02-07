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

from cloudeyeclient.common import manager
from cloudeyeclient.common import utils
from cloudeyeclient.v1 import resource


class AlarmManager(manager.Manager):
    """Cloud Eye alarm API management"""

    resource_class = resource.Alarm

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
            "start": start,
            "limit": limit,
            "order": order
        })
        return self._list('/alarms', key='metric_alarms', params=params)

    def get(self, alarm_id):
        """get alarm"""
        _list = self._list('/alarms/' + alarm_id, key='metric_alarms')
        return _list[0]

    def _change_status(self, alarm_id, enable):
        """_put alarm - enable or disable"""
        json = {
            "alarm_enabled": enable
        }
        return self._update_all('/alarms/%s/action' % alarm_id, json)

    def enable(self, alarm_id):
        """enable alarm"""
        return self._change_status(alarm_id, True)

    def disable(self, alarm_id):
        """disable alarm"""
        return self._change_status(alarm_id, False)

    def delete(self, alarm_id):
        """delete alarm"""
        return self._delete('/alarms/%s' % alarm_id)
