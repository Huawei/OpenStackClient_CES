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
from cloudeyeclient.common.i18n import _


class MetricParser(object):
    namespaces = [
        "SYS.ECS",
        "SYS.EVS",
        "SYS.AS",
        "SYS.ELB",
        "SYS.VPC",
        "SYS.RDS",
        "SYS.WAF",
        "SYS.HVD",
    ]

    @staticmethod
    def add_namespace_arg(parser, required=False):
        parser.add_argument(
            "--namespace",
            required=required,
            # choices=MetricParser.namespaces,
            help=_("list metric with namespace "
                   "(examples: SYS.ECS, SYS.EVS, SYS.AS)")
        )

    @staticmethod
    def add_metric_name_arg(parser, required=False):
        parser.add_argument(
            "--metric-name",
            required=required,
            metavar="<metric-name>",
            help=_("list metric with name(example: cpu_utils)")
        )

    @staticmethod
    def add_dimensions_arg(parser, required=False):
        parser.add_argument(
            "--dimensions",
            required=required,
            metavar="<key=value>",
            default=[],
            action='append',
            help=_("Metric dimension (repeat to set multiple "
                   "dimension, max repeat time is 3)"),
        )

    @staticmethod
    def add_start_arg(parser, required=False):
        parser.add_argument(
            "--start",
            required=required,
            metavar="<key=value>",
            help=_("return result list start from ("
                   "namespace.metric-name.key:value)"),
        )

    @staticmethod
    def add_from_arg(parser, required=True):
        parser.add_argument(
            "--from",
            required=required,
            dest="from_",
            metavar="<timestamp>",
            type=int,
            help=_("Unix timestamp (milliseconds)"),
        )

    @staticmethod
    def add_to_arg(parser, required=True):
        parser.add_argument(
            "--to",
            required=required,
            metavar="<timestamp>",
            type=int,
            help=_("Unix timestamp (milliseconds)"),
        )

    @staticmethod
    def add_period_arg(parser, required=True):
        parser.add_argument(
            "--period",
            required=required,
            choices=["1", "300", "1200", "3600", "14400", "86400"],
            help=_("Monitor granularity (second), "
                   "1 stands for real-time"),
        )

    @staticmethod
    def add_filter_arg(parser, required=True):
        parser.add_argument(
            "--filter",
            required=required,
            choices=["average", "variance", "min", "max"],
            help=_("filter by data aggregation method"),
        )

    @staticmethod
    def add_ttl_arg(parser, required=True):
        parser.add_argument(
            "--ttl",
            required=required,
            metavar="<second>",
            type=int,
            help=_("metric data keeps time(second), max is 604800"),
        )

    @staticmethod
    def add_collect_time_arg(parser, required=True):
        parser.add_argument(
            "--collect-time",
            required=required,
            metavar="<timestamp>",
            type=int,
            help=_("UNIX timestamp"),
        )

    @staticmethod
    def add_value_arg(parser, required=True):
        parser.add_argument(
            "--value",
            required=required,
            metavar="<value>",
            type=float,
            help=_("metric data value"),
        )

    @staticmethod
    def add_unit_arg(parser, required=False):
        parser.add_argument(
            "--unit",
            required=required,
            metavar="<unit>",
            help=_("metric data unit, example: %%, Mb"),
        )

    @staticmethod
    def add_type_arg(parser, required=False):
        parser.add_argument(
            "--type",
            required=required,
            dest="type_",
            choices=["int", "float"],
            help=_("metric data type"),
        )

    @staticmethod
    def add_custom_namespace_arg(parser, required=True):
        parser.add_argument(
            "--namespace",
            metavar="<namespace>",
            required=required,
            help=_("metric namespace (service.item), should not "
                   "starts with SYS, length should be 3-32")
        )


class AlarmParser(object):
    @staticmethod
    def add_start_arg(parser, required=False):
        parser.add_argument(
            "--start",
            required=required,
            metavar="<alarm-id>",
            help=_("list alarms after the alarm-id"),
        )

    @staticmethod
    def add_alarm_id_arg(parser, op):
        parser.add_argument(
            "alarm_id",
            metavar="<alarm-id>",
            help=_("Alarm to be %s (alarm-id)" % op),
        )
