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
from cloudeyeclient.common.i18n import _
from osc_lib.cli import parseractions


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
            metavar="<namespace>",
            choices=MetricParser.namespaces,
            help=_("list metric with namespace")
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
    def add_dim_arg(parser, required=False):
        parser.add_argument(
            "--dim",
            required=required,
            metavar="<key=value>",
            action=parseractions.KeyValueAction,
            help=_("Metric dimension (repeat to set multiple "
                   "dimension, max repeat time is 3)"),
        )

    @staticmethod
    def add_start_arg(parser, required=False):
        parser.add_argument(
            "--start",
            required=required,
            metavar="<key=value>",
            action=parseractions.KeyValueAction,
            help=_("return result list start from ("
                   "namespace.metric-name.key=value)"),
        )