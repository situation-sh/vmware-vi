# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.physical_nic_cdp_device_capability import PhysicalNicCdpDeviceCapability
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PhysicalNicCdpInfo(DataObject):
    """
    CDP (Cisco Discovery Protocol) is a link level protocol that allows for discovering the CDP-awared network hardware at either end of a DIRECT connection.  It's only good for direct connection because CDP doesn't get forwarded through switches. It's a simple advertisement protocol which beacons information about the switch or host along with some port information. The CDP information allows ESX Server admins to know which Cisco switch port is connected to any given virtual switch uplink (PNIC).  ***Since:*** VI API 2.5 
    """ # noqa: E501
    cdp_version: Optional[StrictInt] = Field(default=None, description="CDP version.  The value is always 1.  ***Since:*** VI API 2.5 ", alias="cdpVersion")
    timeout: Optional[StrictInt] = Field(default=None, description="This is the periodicity of advertisement, the time between two successive CDP message transmissions  ***Since:*** VI API 2.5 ")
    ttl: Optional[StrictInt] = Field(default=None, description="Time-To-Live.  the amount of time, in seconds, that a receiver should retain the information contained in the CDP packet.  ***Since:*** VI API 2.5 ")
    samples: Optional[StrictInt] = Field(default=None, description="The number of CDP messages we have received from the device.  ***Since:*** VI API 2.5 ")
    dev_id: Optional[StrictStr] = Field(default=None, description="Device ID which identifies the device.  By default, the device ID is either the device's fully-qualified host name (including the domain name) or the device's hardware serial number in ASCII.  ***Since:*** VI API 2.5 ", alias="devId")
    address: Optional[StrictStr] = Field(default=None, description="The advertised IP address that is assigned to the interface of the device on which the CDP message is sent.  The device can advertise all addresses for a given protocol suite and, optionally, can advertise one or more loopback IP addresses. But this property only show the first address.  ***Since:*** VI API 2.5 ")
    port_id: Optional[StrictStr] = Field(default=None, description="Port ID.  An ASCII character string that identifies the port on which the CDP message is sent, e.g. \"FastEthernet0/8\"  ***Since:*** VI API 2.5 ", alias="portId")
    device_capability: Optional[PhysicalNicCdpDeviceCapability] = Field(default=None, alias="deviceCapability")
    software_version: Optional[StrictStr] = Field(default=None, description="Software version on the device.  A character string that provides information about the software release version that the device is running. e.g. \"Cisco Internetwork Operating Syscisco WS-C2940-8TT-S\"  ***Since:*** VI API 2.5 ", alias="softwareVersion")
    hardware_platform: Optional[StrictStr] = Field(default=None, description="Hardware platform.  An ASCII character string that describes the hardware platform of the device , e.g. \"cisco WS-C2940-8TT-S\"  ***Since:*** VI API 2.5 ", alias="hardwarePlatform")
    ip_prefix: Optional[StrictStr] = Field(default=None, description="IP prefix.  Each IP prefix represents one of the directly connected IP network segments of the local route.  ***Since:*** VI API 2.5 ", alias="ipPrefix")
    ip_prefix_len: Optional[StrictInt] = Field(default=None, description="ipPrefix length.  ***Since:*** VI API 2.5 ", alias="ipPrefixLen")
    vlan: Optional[StrictInt] = Field(default=None, description="The native VLAN of advertising port.  The native VLAN is the VLAN to which a port returns when it is not trunking. Also, the native VLAN is the untagged VLAN on an 802.1Q trunk.  ***Since:*** VI API 2.5 ")
    full_duplex: Optional[StrictBool] = Field(default=None, description="Half/full duplex setting of the advertising port.  ***Since:*** VI API 2.5 ", alias="fullDuplex")
    mtu: Optional[StrictInt] = Field(default=None, description="MTU, the maximum transmission unit for the advertising port.  Possible values are 1500 through 18190.  ***Since:*** VI API 2.5 ")
    system_name: Optional[StrictStr] = Field(default=None, description="The configured SNMP system name of the device.  ***Since:*** VI API 2.5 ", alias="systemName")
    system_oid: Optional[StrictStr] = Field(default=None, description="The configured SNMP system OID of the device.  ***Since:*** VI API 2.5 ", alias="systemOID")
    mgmt_addr: Optional[StrictStr] = Field(default=None, description="The configured IP address of the SNMP management interface for the device.  ***Since:*** VI API 2.5 ", alias="mgmtAddr")
    location: Optional[StrictStr] = Field(default=None, description="The configured location of the device.  ***Since:*** VI API 2.5 ")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PhysicalNicCdpInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PhysicalNicCdpInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


