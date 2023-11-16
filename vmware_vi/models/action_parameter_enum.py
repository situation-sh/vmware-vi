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


class ActionParameterEnum(str, Enum):
    """
    These constant strings can be used as parameters in user-specified email subject and body templates as well as in scripts.  The action processor in VirtualCenter substitutes the run-time values for the parameters. For example, an email subject provided by the client could be the string: `Alarm - {alarmName} Description:\\n{eventDescription}`. Or a script action provided could be: `myScript {alarmName}`.  Possible values: - `targetName`: The name of the entity where the alarm is triggered. - `alarmName`: The name of the triggering alarm. - `oldStatus`: The status prior to the alarm being triggered. - `newStatus`: The status after the alarm is triggered. - `triggeringSummary`: A summary of information involved in triggering the alarm. - `declaringSummary`: A summary of declarations made during the triggering of the alarm. - `eventDescription`: The event description. - `target`: The object of the entity where the alarm is associated. - `alarm`: The object of the triggering alarm. 
    """

    """
    allowed enum values
    """
    TARGETNAME = 'targetName'
    ALARMNAME = 'alarmName'
    OLDSTATUS = 'oldStatus'
    NEWSTATUS = 'newStatus'
    TRIGGERINGSUMMARY = 'triggeringSummary'
    DECLARINGSUMMARY = 'declaringSummary'
    EVENTDESCRIPTION = 'eventDescription'
    TARGET = 'target'
    ALARM = 'alarm'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionParameterEnum from a JSON string"""
        return cls(json.loads(json_str))


