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

from cloudeyeclient.osc.v1 import quota
from cloudeyeclient.tests import base
from cloudeyeclient.v1 import quota_mgr
from cloudeyeclient.v1 import resource


@mock.patch.object(quota_mgr.QuotaManager, "_list")
class TestListMetric(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestListMetric, self).__init__(*args, **kwargs)
        self.quota_list = [
            {
                "type": "alarm",
                "used": 0,
                "unit": "",
                "quota": 20
            }
        ]

    def setUp(self):
        super(TestListMetric, self).setUp()
        self.cmd = quota.ListQuota(self.app, None)

    def test_list_quota(self, mocked_list):
        parsed_args = self.check_parser(
            self.cmd, [], []
        )
        quotas = [resource.Quota(None, q, attached=True)
                  for q in self.quota_list]
        mocked_list.return_value = quotas

        columns, data = self.cmd.take_action(parsed_args)
        mocked_list.assert_called_once_with(
            "/quotas",
            key="quotas.resources",
        )
        self.assertEqual(columns, resource.Quota.list_column_names)
        expect_data = (
            (
                "alarm",
                20,
                0,
                "",
            ),
        )
        self.assertEqual(tuple(data), expect_data)
