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


class Metric(resource.Resource, display.Display):
    """AutoScaling group resource instance."""

    list_column_names = [
        "Namespace",
        "Metric Name",
        "Dimension",
        "Unit"
    ]

    # column_mapping = {
    #     "name": "scaling_group_name",
    #     "status": "scaling_group_status",
    # }

    @property
    def dimension(self):
        if self.dimensions and len(self.dimensions) > 0:
            return [dim['name'] + '=' + dim['value'] for dim in self.dimension]
        return '';

