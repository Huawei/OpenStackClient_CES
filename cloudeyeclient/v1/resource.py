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

from cloudeyeclient.common import display
from cloudeyeclient.common import resource
from cloudeyeclient.common import utils


class Metric(resource.Resource, display.Display):
    """AutoScaling group resource instance."""

    list_column_names = [
        "Namespace",
        "Metric Name",
        "Dimension",
        "Unit"
    ]

    list_favorite_column_names = [
        "Namespace",
        "Metric Name",
        "Dimension",
    ]

    # column_mapping = {
    #     "name": "scaling_group_name",
    #     "status": "scaling_group_status",
    # }

    @property
    def dimension(self):
        if self.dimensions and len(self.dimensions) > 0:
            return ';'.join([dim['name'] + '=' + dim['value']
                             for dim in self.dimensions])
        return '';


def condition_formatter(condition):
    return ("Event {filter}{comparison_operator}{value} occurs {count}"
            " times in {period} seconds").format(**condition);


class Alarm(resource.Resource, display.Display):
    """Cloud Eye alarm resource instance."""

    list_column_names = [
        "id",
        "name",
        "desc",
        "metric namespace",
        "metric name",
        "status"
    ]

    show_column_names = [
        "id",
        "name",
        "desc",
        "metric namespace",
        "metric name",
        "metric dimensions",
        "condition",
        "enabled",
        "action enabled",
        "update time",
        "status"
    ]

    column_2_property = {
        "id": "alarm_id",
        "name": "alarm_name",
        "desc": "alarm_description",
        "enabled": "alarm_enabled",
        "action enabled": "alarm_action_enabled",
        "status": "alarm_state",
    }

    @property
    def metric_namespace(self):
        return self.metric["namespace"]

    @property
    def metric_name(self):
        return self.metric["metric_name"]

    @property
    def metric_dimensions(self):
        dimensions = self.metric['dimensions']
        if dimensions and dimensions > 0:
            return ';'.join([dim['name'] + '=' + dim['value']
                             for dim in dimensions])
        return '';

    formatter = {
        "condition": condition_formatter,
        "update time": utils.format_time
    }


class Quota(resource.Resource, display.Display):
    """Cloud Eye quota resource instance."""

    list_column_names = [
        "type",
        "quota",
        "used",
        "unit",
    ]


class MetricData(resource.Resource, display.Display):
    """Cloud Eye metric data resource instance."""

    formatter = {
        "timestamp": utils.format_time
    }
