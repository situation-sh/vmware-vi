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

from pydantic import Field
from typing_extensions import Annotated
from vmware_vi.models.customization_adapter_mapping import CustomizationAdapterMapping
from vmware_vi.models.customization_global_ip_settings import CustomizationGlobalIPSettings
from vmware_vi.models.customization_identity_settings import CustomizationIdentitySettings
from vmware_vi.models.customization_options import CustomizationOptions
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomizationSpec(DataObject):
    """
    The Specification data object type contains information required to customize a virtual machine when deploying it or migrating it to a new host. 
    """ # noqa: E501
    options: Optional[CustomizationOptions] = None
    identity: CustomizationIdentitySettings
    global_ip_settings: CustomizationGlobalIPSettings = Field(alias="globalIPSettings")
    nic_setting_map: Optional[List[CustomizationAdapterMapping]] = Field(default=None, description="IP settings that are specific to a particular virtual network adapter.  The AdapterMapping object maps a network adapter's MAC address to its Adapter settings object. May be empty if there are no network adapters, else should match number of network adapters in the VM. ", alias="nicSettingMap")
    encryption_key: Optional[List[Annotated[int, Field(le=127, strict=True, ge=-128)]]] = Field(default=None, description="Byte array containing the public key used to encrypt any passwords stored in the specification.  Both the client and the server can use this to determine if stored passwords can be decrypted by the server or if the passwords need to be re-entered and re-encrypted before the specification can be used. ", alias="encryptionKey")
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
        """Create an instance of CustomizationSpec from a JSON string"""
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
        """Create an instance of CustomizationSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


