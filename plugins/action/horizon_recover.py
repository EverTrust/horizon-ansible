#!/usr/bin/python
# -*- coding: utf-8 -*-

# Standard base includes and define this as a metaclass of type
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.errors import AnsibleAction
from ansible_collections.evertrust.horizon.plugins.module_utils.horizon_action import HorizonAction


class ActionModule(HorizonAction):
    TRANSFERS_FILES = True

    def _args(self):
        return ["password", "profile", "certificate_pem"]

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)

        try:
            client = self._get_client()
            content = self._get_content()
            result = client.recover(**content)
            return {
                "p12": response["pkcs12"]["value"],
                "p12_password": response["password"]["value"],
                "key": self.__get_key_from_p12(response["pkcs12"]["value"], response["password"]["value"])
            }

        except AnsibleAction as e:
            result.update(e.result)
