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
from vmware_vi.models.crypto_spec import CryptoSpec
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.key_value import KeyValue
from vmware_vi.models.virtual_machine_profile_spec import VirtualMachineProfileSpec
from vmware_vi.models.vslm_create_spec_backing_spec import VslmCreateSpecBackingSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VslmCreateSpec(DataObject):
    """
    Specification to create a virtual storage object.  ***Since:*** vSphere API 6.5 
    """ # noqa: E501
    name: StrictStr = Field(description="Descriptive name of this virtual storage object.  ***Since:*** vSphere API 6.5 ")
    keep_after_delete_vm: Optional[StrictBool] = Field(default=None, description="Choice of the deletion behavior of this virtual storage object.  If not set, the default value is true.  ***Since:*** vSphere API 6.7 ", alias="keepAfterDeleteVm")
    backing_spec: VslmCreateSpecBackingSpec = Field(alias="backingSpec")
    capacity_in_mb: StrictInt = Field(description="Size in MB of the virtual storage object.  ***Since:*** vSphere API 6.5 ", alias="capacityInMB")
    profile: Optional[List[VirtualMachineProfileSpec]] = Field(default=None, description="Virtual storage object Profile requirement.  If unset, the default behavior will apply.  ***Since:*** vSphere API 6.7 ")
    crypto: Optional[CryptoSpec] = None
    metadata: Optional[List[KeyValue]] = Field(default=None, description="The metadata KV pairs that are supposed to be created on the newly created virtual storage object.  The create task is atomic by design. That being said, failing to add the specified metadata pairs leads to the failure of the create task. If unset, no metadata will be added. An empty string value is indicative of a vcenter tag.  ***Since:*** vSphere API 6.7.2 ")
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
        """Create an instance of VslmCreateSpec from a JSON string"""
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
        """Create an instance of VslmCreateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

