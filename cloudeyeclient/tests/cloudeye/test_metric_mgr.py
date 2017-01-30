#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#   Licensed under the Apache License, Version 2.0 (the 'License'); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import mock
import six
from cloudeyeclient.osc.v1 import metric
from cloudeyeclient.tests import base


class TestMetricMgr(base.BaseTestCase):
    def test_list_metric_args(self):
        list_metric = metric.ListMetric(mock.MagicMock(), mock.MagicMock())
        parser = list_metric.get_parser('list_metric')
        parsed = parser.parse_args([
            '--limit=10',
            '--namespace=SYS.ECS',
            '--metric-name=cpu_util',
            '--order=asc',
            '--start=namespace.metric-name.key:value',
            '--dimensions=key1:value1',
            '--dimensions=key2:value2',
        ])

        self.assertEqual(parsed.limit, 10)
        self.assertEqual(parsed.namespace, "SYS.ECS")
        self.assertEqual(parsed.metric_name, "cpu_util")
        self.assertEqual(parsed.order, "asc")
        self.assertEqual(parsed.start, 'namespace.metric-name.key:value')
        self.assertEqual(parsed.dimension, {'key1': 'value1', 'key2': 'value2'})

        for k in parsed.dimension.keys():
            print k

        dimensions = [k + ',' + v
                      for k, v in six.iteritems(parsed.dimension)]
        self.assertEqual(['key1,value1', 'key2,value2'], dimensions)

    def test_build(self):
        dimensions = ["key,value", "key2,value2"]
        a = ["dim.%d=%s" % (idx, dimension) for (idx, dimension) in enumerate(dimensions)]
        print a