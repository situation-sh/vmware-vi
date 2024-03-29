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
from vmware_vi.models.customization_ip_settings import CustomizationIPSettings
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomizationAdapterMapping(DataObject):
    """
    Data object type to associate a virtual network adapter with its IP settings. 
    """ # noqa: E501
    mac_address: Optional[StrictStr] = Field(default=None, description="The MAC address of a network adapter being customized.  The client cannot change this value because the guest operating system has no control over the MAC address of a virtual network adapter.  This property is optional. If it is not included, the customization process maps the settings from the list of AdapterMappings.IPSettings in the Specification.nicSettingMap to the virtual machine's network adapters, in PCI slot order. The first virtual network adapter on the PCI bus is assigned nicSettingMap\\[0\\].IPSettings, the second adapter is assigned nicSettingMap\\[1\\].IPSettings, and so on.  In vSphere 7.0 series, the MAC addresses must be specified in the ascending order of pciSlotNumber, otherwise a MAC address mismatch error will be reported. For further details, see the https://kb.vmware.com/s/article/87648 ", alias="macAddress")
    adapter: CustomizationIPSettings
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
        """Create an instance of CustomizationAdapterMapping from a JSON string"""
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
        """Create an instance of CustomizationAdapterMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


