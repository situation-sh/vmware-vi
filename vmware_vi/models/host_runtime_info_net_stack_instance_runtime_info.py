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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostRuntimeInfoNetStackInstanceRuntimeInfo(DataObject):
    """
    This data type describes network stack instance runtime info  ***Since:*** vSphere API 5.5 
    """ # noqa: E501
    net_stack_instance_key: StrictStr = Field(description="Key of the instance  ***Since:*** vSphere API 5.5 ", alias="netStackInstanceKey")
    state: Optional[StrictStr] = Field(default=None, description="State of the instance See *HostRuntimeInfoNetStackInstanceRuntimeInfoState_enum* for valid values.  ***Since:*** vSphere API 5.5 ")
    vmknic_keys: Optional[List[StrictStr]] = Field(default=None, description="The keys of vmknics that are using this stack  ***Since:*** vSphere API 5.5 ", alias="vmknicKeys")
    max_number_of_connections: Optional[StrictInt] = Field(default=None, description="The maximum number of socket connections can be worked on this instance currently after booting up.  ***Since:*** vSphere API 5.5 ", alias="maxNumberOfConnections")
    current_ip_v6_enabled: Optional[StrictBool] = Field(default=None, description="If true then dual IPv4/IPv6 stack enabled else IPv4 only.  ***Since:*** vSphere API 5.5 ", alias="currentIpV6Enabled")
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
        """Create an instance of HostRuntimeInfoNetStackInstanceRuntimeInfo from a JSON string"""
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
        """Create an instance of HostRuntimeInfoNetStackInstanceRuntimeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

