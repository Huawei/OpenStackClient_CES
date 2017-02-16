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

from cloudeyeclient.common.i18n import _
from cloudeyeclient.v1 import resource
from osc_lib.command import command

LOG = logging.getLogger(__name__)


class ListQuota(command.Lister):
    _description = _("list quota")

    def get_parser(self, prog_name):
        parser = super(ListQuota, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        quota_mgr = self.app.client_manager.cloudeye.quota_mgr
        quotas = quota_mgr.list()
        columns = resource.Quota.list_column_names
        return columns, (q.get_display_data(columns) for q in quotas)
