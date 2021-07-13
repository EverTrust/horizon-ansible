# horizon.py

import requests, string, random

from ansible.errors import AnsibleError
from requests.exceptions import HTTPError

class Horizon():
    """ La classe Horizon """

    def __init__(self, endpoint, id, key):
        self.endpoint = endpoint
        self._set_headers(id, key)


    def _set_headers(self, id, key):
        ''' set the headers '''
        self.headers = {"x-api-id": id, "x-api-key": key}


    def _get_template(self, module, profile, workflow):
        ''' Get the template of the certificate request on the API. '''

        data =  { "module": module, 
                    "profile": profile, 
                    "workflow": workflow
                }

        try:
            self.template = requests.post(self.endpoint, headers=self.headers, json=data).json()

            if workflow == "enroll":
                self.password_mode = self.template["webRAEnrollRequestTemplate"]["capabilities"]["p12passwordMode"]
                self.password_policy = self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]

            return self.template

        except HTTPError as http_err:
            raise AnsibleError(f'HTTP error occurred: {http_err}')
        except Exception as err:
            raise AnsibleError(f'Other error occurred: {err}')


    def _set_password(self, password=None):
        ''' Generate a random password if no one has been specified '''

        if password != None:
            if self._check_password_policy(password):
                return password
            else :
                if self.password_mode == "manual":
                    raise AnsibleError(f'Your password doesn\'t match with the password policy requiered.' +
                    f'The password has to contains between { self.password_policy["minChar"] } and { self.password_policy["maxChar"] } characters, ' +
                    f'it has to contains at least : { self.password_policy["minLoChar"] } lowercase letter, { self.password_policy["minUpChar"] } uppercase letter, ' +
                    f'{ self.password_policy["minDiChar"] } number, { self.password_policy["minSpChar"] } symbol characters in [ { self.password_policy["spChar"] } ]'
                )
                elif self.password_mode == "random":
                    pass
        
        else:
            if self.password_mode == "manual":
                raise AnsibleError(f'A password is required')
            
            else:
                if "passworPolicy" in self.template["webRAEnrollRequestTemplate"]:
                    whiteList = []
                    
                    for s in self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["spChar"]:
                        whiteList.append(s)

                    for i in range (self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minLoChar"]):
                        self.password += random.choice(string.ascii_lowercase)
                    for i in range (self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minUpChar"]):
                        self.password += random.choice(string.ascii_uppercase)
                    for i in range (self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minDiChar"]):
                        self.password += random.choice(string.digits)
                    for i in range (self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minSpChar"]):
                        self.password += random.choice(whiteList)
                    
                    characters = string.ascii_letters + string.digits + whiteList
                    self.password += (random.choice(characters) for i in range(16 - len(self.password)))
                    if self._check_password_policy(self.password):
                        return self.password
                
                else:
                    characters = string.ascii_letters + string.digits + string.punctuation
                    self.password = ''.join(random.choice(characters) for i in range(16))
                    return self.password

    
    def _check_password_policy(self, password):

        if "passwordPolicy" in self.template["webRAEnrollRequestTemplate"]:
            minLo = self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minLoChar"]
            minUp = self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minUpChar"]
            minDi = self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minDiChar"]
            minSp = self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["minSpChar"]
            whiteList = []
            for s in self.template["webRAEnrollRequestTemplate"]["passwordPolicy"]["spChar"]:
                whiteList.append(s)
        else:
            return 1

        for c in password:
            if c in string.digits:
                minDi -= 1
            elif c in string.ascii_lowercase:
                minLo -= 1
            elif c in string.ascii_uppercase:
                minUp -= 1 
            elif c in whiteList:
                minSp -= 1

            else:
                return 0

        if minDi <= 0 and minLo <= 0 and minUp <= 0 and minSp<= 0:          
            return 1
        else:
            return 0