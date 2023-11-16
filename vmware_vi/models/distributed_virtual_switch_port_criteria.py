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
from vmware_vi.models.dynamic_property import DynamicProperty
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DistributedVirtualSwitchPortCriteria(DataObject):
    """
    The criteria specification for selecting ports.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    dynamic_property: Optional[List[DynamicProperty]] = Field(default=None, description="Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future. ", alias="dynamicProperty")
    connected: Optional[StrictBool] = Field(default=None, description="If set, only the connected ports are qualified.  ***Since:*** vSphere API 4.0 ")
    active: Optional[StrictBool] = Field(default=None, description="If set, only the active ports are qualified.  ***Since:*** vSphere API 4.0 ")
    uplink_port: Optional[StrictBool] = Field(default=None, description="If set to true, only the uplink ports are qualified.  If set to false, only non-uplink ports are qualified.  ***Since:*** vSphere API 4.0 ", alias="uplinkPort")
    nsx_port: Optional[StrictBool] = Field(default=None, description="If set to true, only the NSX ports are qualified.  If set to false, only non-NSX ports are qualified. NSX ports are ports of NSX port group.  ***Since:*** vSphere API 7.0 ", alias="nsxPort")
    scope: Optional[ManagedObjectReference] = None
    portgroup_key: Optional[List[StrictStr]] = Field(default=None, description="The keys of the portgroup that is used for the scope of *DistributedVirtualSwitchPortCriteria.inside*.  If this property is unset, it means any portgroup. If *DistributedVirtualSwitchPortCriteria.inside* is unset, this property is ignored.  ***Since:*** vSphere API 4.0 ", alias="portgroupKey")
    inside: Optional[StrictBool] = Field(default=None, description="If unset, all ports in the switch are qualified.  If set to true, only ports inside *DistributedVirtualSwitchPortCriteria.portgroupKey* or any portgroup, if not set, are qualified. If set to false, only ports outside *DistributedVirtualSwitchPortCriteria.portgroupKey* or any portgroup, if not set, are qualified.  ***Since:*** vSphere API 4.0 ")
    port_key: Optional[List[StrictStr]] = Field(default=None, description="If set, only the ports of which the key is in the array are qualified.  ***Since:*** vSphere API 4.0 ", alias="portKey")
    host: Optional[List[ManagedObjectReference]] = Field(default=None, description="If set, only the ports that are present in one of the host are qualified.  ***Since:*** vSphere API 6.5  Refers instances of *HostSystem*. ")
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
        """Create an instance of DistributedVirtualSwitchPortCriteria from a JSON string"""
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
        """Create an instance of DistributedVirtualSwitchPortCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


