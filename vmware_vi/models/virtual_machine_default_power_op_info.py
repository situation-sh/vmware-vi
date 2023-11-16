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
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineDefaultPowerOpInfo(DataObject):
    """
    The DefaultPowerOpInfo data object type holds the configured defaults for the power operations on a virtual machine.  The properties indicated whether to do a \"soft\" or guest initiated operation, or a \"hard\" operation. 
    """ # noqa: E501
    power_off_type: Optional[StrictStr] = Field(default=None, description="Describes the default power off type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform power off by using the PowerOff method. - soft - Perform power off by using the ShutdownGuest method. - preset - The preset value is specified in the defaultPowerOffType   section.    This setting is advisory and clients can choose to ignore it. ", alias="powerOffType")
    suspend_type: Optional[StrictStr] = Field(default=None, description="Describes the default suspend type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform suspend by using the Suspend method. - soft - Perform suspend by using the StandbyGuest method. - preset - The preset value is specified in the defaultSuspendType   section.    This setting is advisory and clients can choose to ignore it. ", alias="suspendType")
    reset_type: Optional[StrictStr] = Field(default=None, description="Describes the default reset type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform reset by using the Reset method. - soft - Perform reset by using the RebootGuest method. - preset - The preset value is specified in the defaultResetType   section.    This setting is advisory and clients can choose to ignore it. ", alias="resetType")
    default_power_off_type: Optional[StrictStr] = Field(default=None, description="Default operation for power off: soft or hard ", alias="defaultPowerOffType")
    default_suspend_type: Optional[StrictStr] = Field(default=None, description="Default operation for suspend: soft or hard ", alias="defaultSuspendType")
    default_reset_type: Optional[StrictStr] = Field(default=None, description="Default operation for reset: soft or hard ", alias="defaultResetType")
    standby_action: Optional[StrictStr] = Field(default=None, description="Behavior of virtual machine when it receives the S1 ACPI call. ", alias="standbyAction")
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
        """Create an instance of VirtualMachineDefaultPowerOpInfo from a JSON string"""
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
        """Create an instance of VirtualMachineDefaultPowerOpInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

