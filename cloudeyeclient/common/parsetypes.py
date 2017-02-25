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
import argparse
from datetime import datetime

from osc_lib.i18n import _


def date_type(date_format):
    def wrapped(user_input):
        try:
            return datetime.strptime(user_input, date_format)
        except ValueError:
            tpl = _("%s is not a valid date with format %s")
            msg = tpl % (user_input, date_format)
        raise argparse.ArgumentTypeError(msg)

    return wrapped
