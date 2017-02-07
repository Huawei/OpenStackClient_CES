#   Copyright 2016 Huawei, Inc. All rights reserved.
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

from cloudeyeclient.common import resource as base_resource
from cloudeyeclient.osc.v1 import alarm
from cloudeyeclient.tests import base
from cloudeyeclient.v1 import alarm_mgr
from cloudeyeclient.v1 import resource


@mock.patch.object(alarm_mgr.AlarmManager, "_list")
class TestListAlarm(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestListAlarm, self).__init__(*args, **kwargs)
        self.alarm_list = [
            {
                "alarm_name": "test0911_1825",
                "alarm_description": "",
                "metric": {
                    "namespace": "SYS.ECS",
                    "dimensions": [
                        {
                            "name": "instance_id",
                            "value": "d9112af5-6913-4f3b-bd0a-3f96711e004d"
                        }
                    ],
                    "metric_name": "cpu_util"
                },
                "condition": {
                    "period": 300,
                    "filter": "average",
                    "comparison_operator": ">=",
                    "value": 2,
                    "unit": "Count",
                    "count": 1
                },
                "alarm_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "ok_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "insufficientdata_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "alarm_enabled": True,
                "alarm_action_enabled": False,
                "alarm_id": "al1441967036681YkazZ0deN",
                "update_time": 1442306637795,
                "alarm_state": "ok"
            }
        ]

    def setUp(self):
        super(TestListAlarm, self).setUp()
        self.cmd = alarm.ListAlarm(self.app, None)

    def test_list_alarm(self, mocked_list):
        args = [
            "--start", "10",
            "--limit", "20",
            "--order", "asc"
        ]
        verify_args = [
            ("start", 10),
            ("limit", 20),
            ("order", "asc"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )
        alarms = [resource.Alarm(None, a, attached=True)
                  for a in self.alarm_list]
        mocked_list.return_value = alarms

        columns, data = self.cmd.take_action(parsed_args)
        params = {'start': 10, 'limit': 20, 'order': 'asc'}
        mocked_list.assert_called_once_with(
            "/alarms", key="metric_alarms", params=params
        )
        self.assertEqual(columns, resource.Alarm.list_column_names)
        expect_data = (
            (
                "al1441967036681YkazZ0deN",
                "test0911_1825",
                "",
                "SYS.ECS",
                "cpu_util",
                "ok"
            ),
        )
        self.assertEqual(tuple(data), expect_data)


@mock.patch.object(alarm_mgr.AlarmManager, "_list")
class TestShowAlarm(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestShowAlarm, self).__init__(*args, **kwargs)
        self.alarm_list = [
            {
                "alarm_name": "test0911_1825",
                "alarm_description": "",
                "metric": {
                    "namespace": "SYS.ECS",
                    "dimensions": [
                        {
                            "name": "instance_id",
                            "value": "d9112af5-6913-4f3b-bd0a-3f96711e004d"
                        }
                    ],
                    "metric_name": "cpu_util"
                },
                "condition": {
                    "period": 300,
                    "filter": "average",
                    "comparison_operator": ">=",
                    "value": 2,
                    "unit": "Count",
                    "count": 1
                },
                "alarm_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "ok_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "insufficientdata_actions": [
                    {
                        "type": "notification",
                        "notificationList": []
                    }
                ],
                "alarm_enabled": True,
                "alarm_action_enabled": False,
                "alarm_id": "al1441967036681YkazZ0deN",
                "update_time": 1442306637795,
                "alarm_state": "ok"
            }
        ]

    def setUp(self):
        super(TestShowAlarm, self).setUp()
        self.cmd = alarm.ShowAlarm(self.app, None)

    def test_list_alarm(self, mocked_list):
        alarm_id = "alarm-id"
        args = [alarm_id]
        verify_args = [("alarm_id", alarm_id)]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )
        alarms = [resource.Alarm(None, a, attached=True)
                  for a in self.alarm_list]
        mocked_list.return_value = alarms
        columns, data = self.cmd.take_action(parsed_args)

        mocked_list.assert_called_once_with(
            "/alarms/%s" % alarm_id, key="metric_alarms"
        )
        self.assertEqual(columns, resource.Alarm.show_column_names)
        # expect_data = (
        #     (
        #         "al1441967036681YkazZ0deN",
        #         "test0911_1825",
        #         "",
        #         "SYS.ECS",
        #         "cpu_util",
        #         "ok"
        #     ),
        # )
        formatter = resource.Alarm.formatter
        expect_data = alarms[0].get_display_data(columns, formatter)
        self.assertEqual(tuple(data), expect_data)


@mock.patch.object(alarm_mgr.AlarmManager, "_update_all")
class TestEnableAlarm(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestEnableAlarm, self).__init__(*args, **kwargs)

    def setUp(self):
        super(TestEnableAlarm, self).setUp()
        self.cmd = alarm.EnableAlarm(self.app, None)

    def test_list_alarm(self, mocked):
        alarm_id = "alarm-id"
        args = [alarm_id]
        verify_args = [("alarm_id", alarm_id)]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )
        mocked.return_value = base_resource.StrWithMeta('', 'Request-Id')
        result = self.cmd.take_action(parsed_args)

        params = {'alarm_enabled': True}
        mocked.assert_called_once_with(
            "/alarms/%s/action" % alarm_id, params
        )
        self.assertEqual(result, "Alarm %s has been enabled" % alarm_id)


@mock.patch.object(alarm_mgr.AlarmManager, "_update_all")
class TestDisableAlarm(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestDisableAlarm, self).__init__(*args, **kwargs)

    def setUp(self):
        super(TestDisableAlarm, self).setUp()
        self.cmd = alarm.DisableAlarm(self.app, None)

    def test_list_alarm(self, mocked):
        alarm_id = "alarm-id"
        args = [alarm_id]
        verify_args = [("alarm_id", alarm_id)]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )
        mocked.return_value = base_resource.StrWithMeta('', 'Request-Id')
        result = self.cmd.take_action(parsed_args)

        params = {'alarm_enabled': False}
        mocked.assert_called_once_with(
            "/alarms/%s/action" % alarm_id, params
        )
        self.assertEqual(result, "Alarm %s has been disabled" % alarm_id)


@mock.patch.object(alarm_mgr.AlarmManager, "_delete")
class TestDeleteAlarm(base.CloudEyeV1BaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestDeleteAlarm, self).__init__(*args, **kwargs)

    def setUp(self):
        super(TestDeleteAlarm, self).setUp()
        self.cmd = alarm.DeleteAlarm(self.app, None)

    def test_list_alarm(self, mocked):
        alarm_id = "alarm-id"
        args = [alarm_id]
        verify_args = [("alarm_id", alarm_id)]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )
        mocked.return_value = base_resource.StrWithMeta('', 'Request-Id')
        result = self.cmd.take_action(parsed_args)
        mocked.assert_called_once_with("/alarms/%s" % alarm_id)
        self.assertEqual(result, "Alarm %s has been deleted" % alarm_id)
