#
# Copyright (c) 2015 Blue Box Group, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import types
import yaml


class AutoConf(dict):
    """this class extends a dict and from the outside can behave like one."""

    def __init__(self,default={} ,location_config={}, final_override={}):
        """"""
        self.data_to_output = {}

        self.data_to_output = self.merge(default_config,location_config)
        self.data_to_output = self.merge(data_to_output,final_override)

        super(AutoConf, self).__init__(self.data_to_output)

    def merge(self,x,y):
        """merges nested dictionary objects """
        merged = dict(x,**y)
        xkeys = x.keys()
        for key in xkeys:
            if type(x[key]) is types.DictType and y.has_key(key):
                merged[key] = self.merge(x[key],y[key])

        return merged

    def output_yaml(self):
        """outputs the dict as yaml"""
        return yaml.dump(self.data_to_output, default_flow_style=False)

