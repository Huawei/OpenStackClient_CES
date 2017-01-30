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
        pb.MetricParser.add_dimensions_arg(parser)
        pb.MetricParser.add_start_arg(parser)
        bpb.BaseParser.add_limit_option(parser, 1000)
        bpb.BaseParser.add_order_option(parser)
        return parser

    def take_action(self, args):
        metric_mgr = self.app.client_manager.cloudeye.metric_mgr
        dimensions = [dimension.replace('=', ',')
                      for dimension in args.dimensions]
        start = args.start.replace('=', ':') if args.start else None
        metrics = metric_mgr.list(namespace=args.namespace,
                                  metric_name=args.metric_name,
                                  dimensions=dimensions,
                                  start=start,
                                  limit=args.limit,
                                  order=args.order)
        columns = resource.Metric.list_column_names
        return columns, (m.get_display_data(columns) for m in metrics)


class ListFavoriteMetric(command.Lister):
    _description = _("list favorite metrics")

    def get_parser(self, prog_name):
        parser = super(ListFavoriteMetric, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        metric_mgr = self.app.client_manager.cloudeye.metric_mgr
        metrics = metric_mgr.list_favorite()
        columns = resource.Metric.list_favorite_column_names
        return columns, (m.get_display_data(columns) for m in metrics)


class ListMetricData(command.Lister):
    _description = _("list metric data")

    def get_parser(self, prog_name):
        parser = super(ListMetricData, self).get_parser(prog_name)
        pb.MetricParser.add_namespace_arg(parser, True)
        pb.MetricParser.add_metric_name_arg(parser, True)
        pb.MetricParser.add_from_arg(parser)
        pb.MetricParser.add_to_arg(parser)
        pb.MetricParser.add_period_arg(parser)
        pb.MetricParser.add_filter_arg(parser)
        pb.MetricParser.add_dimensions_arg(parser, True)
        return parser

    def take_action(self, args):
        metric_mgr = self.app.client_manager.cloudeye.metric_mgr
        dimensions = [dimension.replace('=', ',')
                      for dimension in args.dimensions]
        data = metric_mgr.list_metric_data(namespace=args.namespace,
                                           metric_name=args.metric_name,
                                           from_=args.from_,
                                           to=args.to,
                                           period=args.period,
                                           filter_=args.filter,
                                           dimensions=dimensions)
        columns = ["timestamp", args.filter, "unit"]
        return columns, (r.get_display_data(columns) for r in data)


class AddMetricData(command.Command):
    _description = _("add metric data")

    def get_parser(self, prog_name):
        parser = super(AddMetricData, self).get_parser(prog_name)
        pb.MetricParser.add_custom_namespace_arg(parser, True)
        pb.MetricParser.add_metric_name_arg(parser, True)
        pb.MetricParser.add_dimensions_arg(parser, True)
        pb.MetricParser.add_ttl_arg(parser, True)
        pb.MetricParser.add_collect_time_arg(parser, True)
        pb.MetricParser.add_value_arg(parser, True)
        pb.MetricParser.add_unit_arg(parser, False)
        pb.MetricParser.add_type_arg(parser, False)
        return parser

    def take_action(self, args):
        metric_mgr = self.app.client_manager.cloudeye.metric_mgr
        dimensions = []
        for dimension in args.dimensions:
            split = dimension.split("=")
            dimensions.append({
                "name": split[0],
                "value": split[1]
            })
        data = metric_mgr.add_metric_data(namespace=args.namespace,
                                          metric_name=args.metric_name,
                                          dimensions=dimensions,
                                          ttl=args.ttl,
                                          collect_time=args.collect_time,
                                          value=args.value,
                                          unit=args.unit,
                                          type_=args.type_)
        return 'Metric data has been added'
