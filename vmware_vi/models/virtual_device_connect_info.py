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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualDeviceConnectInfo(DataObject):
    """
    The <code>*VirtualDeviceConnectInfo*</code> data object type contains information about connectable virtual devices. 
    """ # noqa: E501
    migrate_connect: Optional[StrictStr] = Field(default=None, description="Specifies whether the virtual machine should override the virtual device connection state upon the completion of a migration.  At this time, this property is only applicable to instant clone operations, and will be ignored for other migration types. The property is also only valid with VirtualEthernetCards, and any attempt to set this property on an unsupported device will result in an error. This property will persist only until the virtual machine undergoes a supported migration, at which point it will be consumed and unset on the destination virtual machine, preventing the property from affecting future migrations. The migration's success is not dependent on whether the device reaches the desired connection state. The set of possible values are described in *VirtualDeviceConnectInfoMigrateConnectOp_enum*.  ***Since:*** vSphere API 6.7 ", alias="migrateConnect")
    start_connected: StrictBool = Field(description="Specifies whether or not to connect the device when the virtual machine starts. ", alias="startConnected")
    allow_guest_control: StrictBool = Field(description="Enables guest control over whether the connectable device is connected. ", alias="allowGuestControl")
    connected: StrictBool = Field(description="Indicates whether the device is currently connected.  Valid only while the virtual machine is running. ")
    status: Optional[StrictStr] = Field(default=None, description="Indicates the current status of the connectable device.  Valid only while the virtual machine is running. The set of possible values is described in *VirtualDeviceConnectInfoStatus_enum*  ***Since:*** vSphere API 4.0 ")
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
        """Create an instance of VirtualDeviceConnectInfo from a JSON string"""
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
        """Create an instance of VirtualDeviceConnectInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


