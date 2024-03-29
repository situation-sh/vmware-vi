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


class ClusterVmComponentProtectionSettingsStorageVmReactionEnum(str, Enum):
    """
    The VM policy settings that determine the response to storage failures.  Possible values: - `disabled`: VM Component Protection service will not monitor or react to   the component failure.      This setting does not affect other vSphere   HA services such as Host Monitoring or VM Health Monitoring. - `warning`: VM Component Protection service will monitor component failures but   will not restart an affected VM.      Rather it will notify users about   the component failures. This setting does not affect other vSphere HA   services such as Host Monitoring or VM Health Monitoring. - `restartConservative`: VM Component Protection service protects VMs conservatively.      With this   setting, when the service can't determine that capacity is available to   restart a VM, it will favor keeping the VM running. - `restartAggressive`: VM Component Protection service protects VMs aggressively.      With this setting,   the service will terminate an affected VM even if it can't determine that   capacity exists to restart the VM. - `clusterDefault`: VM will use the cluster default setting.      This option is only meaningful for   per-VM settings.  ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    DISABLED = 'disabled'
    WARNING = 'warning'
    RESTARTCONSERVATIVE = 'restartConservative'
    RESTARTAGGRESSIVE = 'restartAggressive'
    CLUSTERDEFAULT = 'clusterDefault'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterVmComponentProtectionSettingsStorageVmReactionEnum from a JSON string"""
        return cls(json.loads(json_str))


