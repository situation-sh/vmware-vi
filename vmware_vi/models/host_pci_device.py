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
from pydantic import StrictStr
from pydantic import Field
from typing_extensions import Annotated
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostPciDevice(DataObject):
    """
    This data object type describes information about a single Peripheral Component Interconnect (PCI) device. 
    """ # noqa: E501
    id: StrictStr = Field(description="The name ID of this PCI, composed of \"bus:slot.function\". ")
    class_id: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="The class of this PCI. ", alias="classId")
    bus: Annotated[int, Field(le=127, strict=True, ge=-128)] = Field(description="The bus ID of this PCI. ")
    slot: Annotated[int, Field(le=127, strict=True, ge=-128)] = Field(description="The slot ID of this PCI. ")
    function: Annotated[int, Field(le=127, strict=True, ge=-128)] = Field(description="The function ID of this PCI. ")
    vendor_id: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="The vendor ID of this PCI.  The vendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI vendor ID. The WSDL representation of the ID is a signed short integer. If the vendor ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. When you specify a PCI device vendor ID for a virtual machine (*VirtualPCIPassthroughDeviceBackingInfo*.vendorId), you must use the retrieved *HostPciDevice*.deviceId value. ", alias="vendorId")
    sub_vendor_id: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="The subvendor ID of this PCI.  The subvendor ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subvendor ID. The WSDL representation of the ID is a signed short integer. If the subvendor ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. ", alias="subVendorId")
    vendor_name: StrictStr = Field(description="The vendor name of this PCI. ", alias="vendorName")
    device_id: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="The device ID of this PCI.  The device ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI device ID. The WSDL representation of the ID is a signed short integer. If the PCI ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. When you specify a PCI device ID for a virtual machine (*VirtualPCIPassthroughDeviceBackingInfo*.deviceId), you must use the *HostPciDevice*.deviceId value as retrieved and convert it to a string. ", alias="deviceId")
    sub_device_id: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="The subdevice ID of this PCI.  The subdevice ID might be a negative value. A vSphere Server uses an unsigned short integer to represent a PCI subdevice ID. The WSDL representation of the ID is a signed short integer. If the subdevice ID is greater than 32767, the Server will convert the ID to its two's complement for the WSDL representation. ", alias="subDeviceId")
    parent_bridge: Optional[StrictStr] = Field(default=None, description="The parent bridge of this PCI.  ***Since:*** vSphere API 4.0 ", alias="parentBridge")
    device_name: StrictStr = Field(description="The device name of this PCI. ", alias="deviceName")
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
        """Create an instance of HostPciDevice from a JSON string"""
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
        """Create an instance of HostPciDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


