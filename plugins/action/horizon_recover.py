# horizon_recover.py

# Standard base includes and define this as a metaclass of type
from __future__ import (absolute_import, division, print_function)

from ansible_collections.evertrust.horizon.plugins.module_utils.horizon import Horizon

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    TRANSFERS_FILES = True

    def run(self, tmp=None, task_vars=None):

        # Get value from playbook
        self._get_all_informations()
        # Initialize the class Horizon
        self.horizon = Horizon(self.endpoint_t, self.id, self.key)
        # Save the template in a self variable
        self.template = self.horizon._get_template(self.module, self.profile, "recover")
        # Set or verify the password
        self.password = self.horizon._set_password(self.password) 
        
        my_json = self.horizon._generate_json(module=self.module, profile=self.profile, password=self.password, workflow="recover", certificate_pem=self.certificate_pem)
        
        return self.horizon._post_request(self.endpoint_s, my_json)
        
    

    def _get_all_informations(self):
        ''' Save all plugin information in self variables '''
        self.endpoint_t = self._task.args.get('endpoint_template')
        self.endpoint_s = self._task.args.get('endpoint_request')
        self.id = self._task.args.get('x-api-id')
        self.key = self._task.args.get('x-api-key')
        self.module = self._task.args.get('module')
        self.profile = self._task.args.get('profile')
        self.password = self._task.args.get('password')
        self.certificate_pem = self._task.args.get('certificatePem')