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


from typing import Any, ClassVar, Dict, List
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualUSBRemoteHostBackingInfo(VirtualDeviceDeviceBackingInfo):
    """
    The *VirtualUSBRemoteHostBackingInfo* data object identifies a host and a USB device that is attached to the host.  Use this object to configure support for persistent access to the USB device when vMotion operations migrate a virtual machine to a different host. The vCenter Server will not migrate the virtual machine to a host that does not support the USB remote host backing capability.  Specify remote host backing as part of the USB device configuration when you create or reconfigure a virtual machine (*VirtualMachineConfigSpec*.*VirtualMachineConfigSpec.deviceChange*.*VirtualDeviceConfigSpec.device*.*VirtualDevice.backing*).  To identify the USB device, you specify an autoconnect pattern for the *VirtualDeviceDeviceBackingInfo.deviceName*. The virtual machine can connect to the USB device if the ESX server can find a USB device described by the autoconnect pattern. The autoconnect pattern consists of name:value pairs. You can use any combination of the following fields. - path - USB connection path on the host - pid - idProduct field in the USB device descriptor - vid - idVendor field in the USB device descriptor - hostId - unique ID for the host - speed - device speed (low, full, or high)    For example, the following pattern identifies a USB device:  &nbsp;&nbsp;&nbsp;&nbsp;<code>\"path:1/3/0 hostId:44\\\\ 45\\\\ 4c\\\\ 43\\\\ 00\\\\ 10\\\\ 54-80\\\\ 35\\\\ ca\\\\ c0\\\\ 4f\\\\ 4d\\\\ 37\\\\ 31\"</code>  This pattern identifies the USB device connected to port 1/3/0 on the host with the unique id <code>0x44454c4c430010548035cac04f4d3731</code>.  Special characters for autoconnect pattern values: - The name and value are separated by a colon (:). - Name:value pairs are separated by spaces. - The escape character is a backslash (\\\\). Use a single backslash to embed   a space in a value. Use a double blackslash to embed a single backslash   in the value.    ***Since:*** vSphere API 4.1 
    """ # noqa: E501
    hostname: StrictStr = Field(description="Name of the ESX host to which the physical USB device is attached (*HostSystem*.*ManagedEntity.name*).  When you configure remote host backing, hostname must identify the local host on which the virtual machine is running.  ***Since:*** vSphere API 4.1 ")
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
        """Create an instance of VirtualUSBRemoteHostBackingInfo from a JSON string"""
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
        """Create an instance of VirtualUSBRemoteHostBackingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


