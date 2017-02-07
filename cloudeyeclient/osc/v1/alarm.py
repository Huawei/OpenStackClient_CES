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
import logging

from osc_lib.command import command

from cloudeyeclient.common import parser_builder as bpb
from cloudeyeclient.common.i18n import _
from cloudeyeclient.osc.v1 import parser_builder as pb
from cloudeyeclient.v1 import resource

LOG = logging.getLogger(__name__)


class ListAlarm(command.Lister):
    _description = _("list alarm")

    def get_parser(self, prog_name):
        parser = super(ListAlarm, self).get_parser(prog_name)
        pb.AlarmParser.add_start_arg(parser)
        bpb.BaseParser.add_limit_option(parser, 100)
        bpb.BaseParser.add_order_option(parser)
        return parser

    def take_action(self, args):
        alarm_mgr = self.app.client_manager.cloudeye.alarm_mgr
        alarms = alarm_mgr.list(start=args.start,
                                limit=args.limit,
                                order=args.order)
        columns = resource.Alarm.list_column_names
        return columns, (a.get_display_data(columns) for a in alarms)


class ShowAlarm(command.ShowOne):
    _description = _("show alarm")

    def get_parser(self, prog_name):
        parser = super(ShowAlarm, self).get_parser(prog_name)
        pb.AlarmParser.add_alarm_id_arg(parser, 'shown')
        return parser

    def take_action(self, args):
        alarm_mgr = self.app.client_manager.cloudeye.alarm_mgr
        alarm = alarm_mgr.get(args.alarm_id)
        columns = resource.Alarm.show_column_names
        formatter = resource.Alarm.formatter
        return columns, alarm.get_display_data(columns, formatter)


class EnableAlarm(command.Command):
    _description = _("enable alarm")

    def get_parser(self, prog_name):
        parser = super(EnableAlarm, self).get_parser(prog_name)
        pb.AlarmParser.add_alarm_id_arg(parser, 'enabled')
        return parser

    def take_action(self, args):
        alarm_mgr = self.app.client_manager.cloudeye.alarm_mgr
        alarm_mgr.enable(args.alarm_id)
        return "Alarm %s has been enabled" % args.alarm_id


class DisableAlarm(command.Command):
    _description = _("disable alarm")

    def get_parser(self, prog_name):
        parser = super(DisableAlarm, self).get_parser(prog_name)
        pb.AlarmParser.add_alarm_id_arg(parser, 'disabled')
        return parser

    def take_action(self, args):
        alarm_mgr = self.app.client_manager.cloudeye.alarm_mgr
        alarm_mgr.disable(args.alarm_id)
        return "Alarm %s has been disabled" % args.alarm_id


class DeleteAlarm(command.Command):
    _description = _("disable alarm")

    def get_parser(self, prog_name):
        parser = super(DeleteAlarm, self).get_parser(prog_name)
        pb.AlarmParser.add_alarm_id_arg(parser, 'disabled')
        return parser

    def take_action(self, args):
        alarm_mgr = self.app.client_manager.cloudeye.alarm_mgr
        alarm_mgr.delete(args.alarm_id)
        return "Alarm %s has been deleted" % args.alarm_id
