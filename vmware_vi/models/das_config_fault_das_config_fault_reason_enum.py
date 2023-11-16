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


class DasConfigFaultDasConfigFaultReasonEnum(str, Enum):
    """
    Possible values: - `HostNetworkMisconfiguration`: There is a problem with the host network configuration. - `HostMisconfiguration`: There is a problem with the host configuration. - `InsufficientPrivileges`: The privileges were insuffient for the operation. - `NoPrimaryAgentAvailable`: There was no running primary agent available to contact.      Check that your other hosts don't have HA errors - `Other`: The HA configuration failed for other reasons. - `NoDatastoresConfigured`: No datastores defined for this host      ***Since:*** vSphere API 5.1 - `CreateConfigVvolFailed`: Failure to create config vvol      ***Since:*** vSphere API 6.0 - `VSanNotSupportedOnHost`: Host in vSAN cluster does not support vSAN.      ***Since:*** vSphere API 5.5 - `DasNetworkMisconfiguration`: There is a problem with the cluster network configuration.      ***Since:*** vSphere API 6.0 - `SetDesiredImageSpecFailed`: Setting desired imageSpec in Personality Manager failed      ***Since:*** vSphere API 7.0 - `ApplyHAVibsOnClusterFailed`: The ApplyHA call to Personality Manager failed      ***Since:*** vSphere API 7.0  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    HOSTNETWORKMISCONFIGURATION = 'HostNetworkMisconfiguration'
    HOSTMISCONFIGURATION = 'HostMisconfiguration'
    INSUFFICIENTPRIVILEGES = 'InsufficientPrivileges'
    NOPRIMARYAGENTAVAILABLE = 'NoPrimaryAgentAvailable'
    OTHER = 'Other'
    NODATASTORESCONFIGURED = 'NoDatastoresConfigured'
    CREATECONFIGVVOLFAILED = 'CreateConfigVvolFailed'
    VSANNOTSUPPORTEDONHOST = 'VSanNotSupportedOnHost'
    DASNETWORKMISCONFIGURATION = 'DasNetworkMisconfiguration'
    SETDESIREDIMAGESPECFAILED = 'SetDesiredImageSpecFailed'
    APPLYHAVIBSONCLUSTERFAILED = 'ApplyHAVibsOnClusterFailed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DasConfigFaultDasConfigFaultReasonEnum from a JSON string"""
        return cls(json.loads(json_str))

