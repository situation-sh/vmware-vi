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


class HostRdmaDeviceConnectionStateEnum(str, Enum):
    """
    Possible RDMA device connection states.  These correspond to possible link states as defined by the Infiniband (TM) specification.  Further details can be found in: - \"Infiniband (TM) Architecture Specification, Volume 1\"   section 7.2 \"Link states\"    Possible values: - `unknown`: Connection state unknown.      Indicates that the driver returned   unexpected or no connection state information. - `down`: Device down.      Indicates that both the logical link and   underlying physical link are down. Packets   are discarded. - `init`: Device initializing.      Indicates that the physical link is up, but   the logical link is still initializing.   Only subnet management and flow control link   packets can be received and transmitted. - `armed`: Device armed.      Indicates that the physical link is up, but   the logical link is not yet fully configured.   Packets can be received, but non-SMPs   (subnet management packets) to be sent are discarded. - `active`: Device active.      Indicates that both the physical and logical   link are up. Packets can be transmitted and received. - `activeDefer`: Device in active defer state.      Indicates that the logical link was active, but the   physical link has suffered a failure. If it recovers   within a timeout, the connection state will return to active,   otherwise it will move to down.  ***Since:*** vSphere API 7.0 
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    DOWN = 'down'
    INIT = 'init'
    ARMED = 'armed'
    ACTIVE = 'active'
    ACTIVEDEFER = 'activeDefer'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostRdmaDeviceConnectionStateEnum from a JSON string"""
        return cls(json.loads(json_str))

