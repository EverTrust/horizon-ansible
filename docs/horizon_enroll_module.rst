.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.evertrust.horizon.horizon_enroll_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

evertrust.horizon.horizon_enroll -- Horizon enrollment plugin
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `evertrust.horizon collection <https://galaxy.ansible.com/evertrust/horizon>`_ (version 0.1.1).

    To install it use: :code:`ansible-galaxy collection install evertrust.horizon`.

    To use it in a playbook, specify: :code:`evertrust.horizon.horizon_enroll`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Performs an enrollment against the Horizon API.

.. note::
    This module has a corresponding :ref:`action plugin <action_plugins>`.

.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- cryptography>=3.4.0


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ca_bundle"></div>
                    <b>ca_bundle</b>
                    <a class="ansibleOptionLink" href="#parameter-ca_bundle" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The location of a CA Bundle to use when validating SSL certificates.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-client_cert"></div>
                    <b>client_cert</b>
                    <a class="ansibleOptionLink" href="#parameter-client_cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The location of a client side certificate.</div>
                                            <div>Required if you use certificate authentication</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-client_key"></div>
                    <b>client_key</b>
                    <a class="ansibleOptionLink" href="#parameter-client_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The location of a client side certificate&#x27;s key.</div>
                                            <div>Required if you use certificate authentication</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-endpoint"></div>
                    <b>endpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-endpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Horizon installation endpoint</div>
                                            <div>Should include the protocol (https://) and no trailing slash</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-key_type"></div>
                    <b>key_type</b>
                    <a class="ansibleOptionLink" href="#parameter-key_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Type of key to encode</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels of the certificate</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-mode"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>centralized</li>
                                                                                                                                                                                                <li>decentralized</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>enrollement mode</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Security password for the certificate.</div>
                                            <div>Password policies will be applied to check validity.</div>
                                            <div>Required only if the enrollement is centralized and the password generation mode is not random.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-profile"></div>
                    <b>profile</b>
                    <a class="ansibleOptionLink" href="#parameter-profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the profile that will be used to enroll the certificate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sans"></div>
                    <b>sans</b>
                    <a class="ansibleOptionLink" href="#parameter-sans" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Subject alternative names of the certificate</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-subject"></div>
                    <b>subject</b>
                    <a class="ansibleOptionLink" href="#parameter-subject" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Certificate subject.</div>
                                            <div>You can either give the description of the subject, or the full dn.</div>
                                            <div>If you give the dn, other values won&#x27;t be used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-x_api_id"></div>
                    <b>x_api_id</b>
                    <a class="ansibleOptionLink" href="#parameter-x_api_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Horizon identifier</div>
                                            <div>Required if you use password authentication</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-x_api_key"></div>
                    <b>x_api_key</b>
                    <a class="ansibleOptionLink" href="#parameter-x_api_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Horizon password</div>
                                            <div>Required if you use password authentication</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - Enrolling a certificate requires permissions on the related profile.
   - Be sure to use the "Enroll API" permission instead of "Enroll".

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Simple centralized enrollment
      evertrust.horizon.horizon_enroll:
        # login and password to connect to the API
        endpoint: "https://<api-endpoint>"
        x_api_id: "<horizon-id>"
        x_api_key: "<horizon-password>"
        mode: "centralized"
        password: "pAssw0rd"
        key_type: "rsa-2048"
        profile: "profile"
        subject:
          cn.1: "myCN"
        sans:
          dnsname.1: "myDnsname"
        labels:
          snow_id: "value1"
          exp_tech: "value2"
    - name: decentralized enrollment with csr
      evertrust.horizon.horizon_enroll:
        # login and password to connect to the API
        endpoint: "https://<api-endpoint>"
        x_api_id: "<horizon-id>"
        x_api_key: "<horizon-password>"
        mode: "decentralized"
        csr: <a_csr_file>
        password: "pAssw0rd"
        key_type: "rsa-2048"
        profile: "profile"
        subject:
          cn.1: "myCN"
          ou.1: "myFirstOU"
          ou.2: "mySecondOU"
        sans:
          dnsname:
            - "myDnsName1"
            - "myDnsName2"
        labels:
          snow_id: "value1"
          exp_tech: "value2"
    - name: decentralized enrollment without csr
      evertrust.horizon.horizon_enroll:
        # login and password to connect to the API
        endpoint: "https://<api-endpoint>"
        x_api_id: "<horizon-id>"
        x_api_key: "<horizon-password>"
        mode: "decentralized"
        password: "pAssw0rd"
        key_type: "rsa-2048"
        profile: "profile"
        subject:
          cn.1: "myCN"
          ou:
            - "myFirstOU"
            - "mySecondOU"
        sans:
          dnsname.1: "myDnsname"
        labels:
          snow_id: "value1"
          exp_tech: "value2"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-certificate"></div>
                    <b>certificate</b>
                    <a class="ansibleOptionLink" href="#return-certificate" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Certificate enrolled</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>if enrollement mode is &quot;centralized&quot;</td>
                <td>
                                            <div>Public key of the certificate</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-p12"></div>
                    <b>p12</b>
                    <a class="ansibleOptionLink" href="#return-p12" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>If enrollement mode is &quot;centralized&quot;</td>
                <td>
                                            <div>PKCS#12 returned by the API</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-p12_password"></div>
                    <b>p12_password</b>
                    <a class="ansibleOptionLink" href="#return-p12_password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>If enrollement mode is &quot;centralized&quot;</td>
                <td>
                                            <div>Password used to enroll</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Evertrust R&D (@EverTrust)



.. Parsing errors
