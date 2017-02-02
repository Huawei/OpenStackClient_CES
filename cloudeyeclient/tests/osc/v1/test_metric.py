#   Copyright 2016 Huawei, Inc. All rights reserved.
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
import mock

from cloudeyeclient.osc.v1 import metric
from cloudeyeclient.tests import base
from cloudeyeclient.v1 import metric_mgr
from cloudeyeclient.v1 import resource


@mock.patch.object(metric_mgr.MetricManager, "_list")
class TestListMetric(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestListMetric, self).__init__(*args, **kwargs)
        self.metric_list = [
            {
                "namespace": "SYS.ECS",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "d9112af5-6913-4f3b-bd0a-3f96711e004d"
                    }
                ],
                "metric_name": "cpu_util",
                "unit": "%"
            }
        ]

    def setUp(self):
        super(TestListMetric, self).setUp()
        self.cmd = metric.ListMetric(self.app, None)

    def test_list_metric(self, mocked_list):
        dimension_1 = "bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4"
        dimension_2 = "instance_id=5b4c1602-fb6d-4f1e-87a8-dcf21d9654ba"
        start = ("SYS.ECS.cpu_util.instance_id="
                 "d9112af5-6913-4f3b-bd0a-3f96711e004d")
        args = [
            "--namespace", "SYS.ECS",
            "--metric-name", "cpu_util",
            "--start", start,
            "--limit", "100",
            "--order", "asc",
            "--dimensions", dimension_1,
            "--dimensions", dimension_2
        ]

        verify_args = [
            ("namespace", "SYS.ECS"),
            ("metric_name", "cpu_util"),
            ("start", start),
            ("limit", 100),
            ("order", "asc"),
            ("dimensions", [dimension_1, dimension_2]),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        metrics = [resource.Metric(None, m, attached=True)
                   for m in self.metric_list]

        mocked_list.return_value = metrics
        columns, data = self.cmd.take_action(parsed_args)

        params = {
            "namespace": "SYS.ECS",
            "metric_name": "cpu_util",
            "start": start.replace('=', ':'),
            "dim.0": dimension_1.replace('=', ','),
            "dim.1": dimension_2.replace('=', ','),
            "limit": 100,
            "order": "asc"
        }
        mocked_list.assert_called_once_with(
            "/metrics",
            key="metrics",
            params=params,
        )
        self.assertEqual(columns, resource.Metric.list_column_names)
        expect_data = (
            (
                "SYS.ECS",
                "cpu_util",
                "instance_id=d9112af5-6913-4f3b-bd0a-3f96711e004d",
                "%",
            ),
        )
        self.assertEqual(tuple(data), expect_data)


@mock.patch.object(metric_mgr.MetricManager, "_list")
class TestListFavoriteMetric(base.CloudEyeV1BaseTestCase):

    def __init__(self, *args, **kwargs):
        super(TestListFavoriteMetric, self).__init__(*args, **kwargs)
        self.metric_list = [
            {
                "namespace": "SYS.ECS",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "d9112af5-6913-4f3b-bd0a-3f96711e004d"
                    }
                ],
                "metric_name": "cpu_util",
                "unit": "%"
            }
        ]

    def setUp(self):
        super(TestListFavoriteMetric, self).setUp()
        self.cmd = metric.ListFavoriteMetric(self.app, None)

    def test_list_metric(self, mocked_list):
        parsed_args = self.check_parser(
            self.cmd, [], []
        )
        metrics = [resource.Metric(None, m, attached=True)
                   for m in self.metric_list]
        mocked_list.return_value = metrics
        columns, data = self.cmd.take_action(parsed_args)

        mocked_list.assert_called_once_with(
            "/favorite-metrics",
            key="metrics",
        )
        self.assertEqual(columns, resource.Metric.list_favorite_column_names)
        expect_data = (
            (
                "SYS.ECS",
                "cpu_util",
                "instance_id=d9112af5-6913-4f3b-bd0a-3f96711e004d",
            ),
        )
        self.assertEqual(tuple(data), expect_data)