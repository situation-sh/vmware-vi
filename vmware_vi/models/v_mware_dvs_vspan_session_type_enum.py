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


class VMwareDVSVspanSessionTypeEnum(str, Enum):
    """
    Distributed Port Mirroring session types.  Possible values: - `mixedDestMirror`:       Deprecated as of vSphere API 5.1.      In mixedDestMirror session, Distributed Ports can be used as source entities,   and both Distributed Ports and Uplink Ports Name can be used as destination entities. - `dvPortMirror`: In dvPortMirror session, Distributed Ports can be used as both source   and destination entities. - `remoteMirrorSource`: In remoteMirrorSource session, Distributed Ports can be used as source entities,   and uplink ports name can be used as destination entities. - `remoteMirrorDest`: In remoteMirrorDest session, vlan Ids can be used as source entities,   and Distributed Ports can be used as destination entities. - `encapsulatedRemoteMirrorSource`: In encapsulatedRemoteMirrorSource session, Distributed Ports can be used as source entities,   and Ip address can be used as destination entities.    ***Since:*** vSphere API 5.1 
    """

    """
    allowed enum values
    """
    MIXEDDESTMIRROR = 'mixedDestMirror'
    DVPORTMIRROR = 'dvPortMirror'
    REMOTEMIRRORSOURCE = 'remoteMirrorSource'
    REMOTEMIRRORDEST = 'remoteMirrorDest'
    ENCAPSULATEDREMOTEMIRRORSOURCE = 'encapsulatedRemoteMirrorSource'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VMwareDVSVspanSessionTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


