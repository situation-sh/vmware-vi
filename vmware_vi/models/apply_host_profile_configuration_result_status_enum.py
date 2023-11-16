# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ApplyHostProfileConfigurationResultStatusEnum(str, Enum):
    """
    Possible values: - `success`: Remediation succeeded. - `failed`: Remediation failed. - `reboot_failed`: Remediation succeeded but reboot after remediation failed.      May treat this as a warning. - `stateless_reboot_failed`: Stateless reboot for remediation failed. - `check_compliance_failed`: Remediation and reboot succeeded but check compliance after reboot   failed.      May treat this as a warning. - `state_not_satisfied`: The required state is not satisfied so host profiel apply cannot   be done. - `exit_maintenancemode_failed`: Exit maintenance mode failed. - `canceled`: The remediation was canceled.    ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    SUCCESS = 'success'
    FAILED = 'failed'
    REBOOT_FAILED = 'reboot_failed'
    STATELESS_REBOOT_FAILED = 'stateless_reboot_failed'
    CHECK_COMPLIANCE_FAILED = 'check_compliance_failed'
    STATE_NOT_SATISFIED = 'state_not_satisfied'
    EXIT_MAINTENANCEMODE_FAILED = 'exit_maintenancemode_failed'
    CANCELED = 'canceled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplyHostProfileConfigurationResultStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


