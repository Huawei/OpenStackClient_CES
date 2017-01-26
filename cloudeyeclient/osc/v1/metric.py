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

from cloudeyeclient.common import parser_builder as bpb
from cloudeyeclient.common.i18n import _
from cloudeyeclient.osc.v1 import parser_builder as pb
from cloudeyeclient.v1 import resource

from osc_lib.command import command

LOG = logging.getLogger(__name__)


class ListMetric(command.Lister):
    _description = _("list metrics")

    def get_parser(self, prog_name):
        parser = super(ListMetric, self).get_parser(prog_name)
        pb.MetricParser.add_namespace_arg(parser)
        pb.MetricParser.add_metric_name_arg(parser)
        pb.MetricParser.add_dim_arg(parser)
        pb.MetricParser.add_start_arg(parser)
        bpb.BaseParser.add_limit_option(parser, 1000)
        bpb.BaseParser.add_order_option(parser)
        return parser

    def take_action(self, args):
        metric_mgr = self.app.client_manager.cloudeye.metric_mgr
        LOG.info(args)
        metrics = metric_mgr.list(namespace=args.namespace,
                                  metric_name=args.metric_name,
                                  dim=args.dim,
                                  start=args.start,
                                  limit=args.limit,
                                  order=args.order)
        columns = resource.Metric.list_column_names
        return columns, (m.get_display_data(columns) for m in metrics)
