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
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DistributedVirtualPortgroupInfo(DataObject):
    """
    This class describes a DistributedVirtualPortgroup that a device backing can be attached to.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    switch_name: StrictStr = Field(description="The name of the switch.  ***Since:*** vSphere API 4.0 ", alias="switchName")
    switch_uuid: StrictStr = Field(description="The UUID of the switch.  ***Since:*** vSphere API 4.0 ", alias="switchUuid")
    portgroup_name: StrictStr = Field(description="The name of the portgroup.  ***Since:*** vSphere API 4.0 ", alias="portgroupName")
    portgroup_key: StrictStr = Field(description="The key of the portgroup.  ***Since:*** vSphere API 4.0 ", alias="portgroupKey")
    portgroup_type: StrictStr = Field(description="The type of portgroup.  See *DistributedVirtualPortgroupPortgroupType_enum*  ***Since:*** vSphere API 4.0 ", alias="portgroupType")
    uplink_portgroup: StrictBool = Field(description="Whether this portgroup is an uplink portgroup.  ***Since:*** vSphere API 4.0 ", alias="uplinkPortgroup")
    portgroup: ManagedObjectReference
    network_reservation_supported: Optional[StrictBool] = Field(default=None, description="Indicates whether network bandwidth reservation is supported on the portgroup  ***Since:*** vSphere API 6.0 ", alias="networkReservationSupported")
    backing_type: Optional[StrictStr] = Field(default=None, description="Backing type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupBackingType_enum* for possible values. The default value is \"standard\".  ***Since:*** vSphere API 7.0 ", alias="backingType")
    logical_switch_uuid: Optional[StrictStr] = Field(default=None, description="The logical switch UUID, which is used by NSX portgroup  ***Since:*** vSphere API 7.0 ", alias="logicalSwitchUuid")
    segment_id: Optional[StrictStr] = Field(default=None, description="The segment ID of logical switch, which is used by NSX portroup  ***Since:*** vSphere API 7.0 ", alias="segmentId")
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
        """Create an instance of DistributedVirtualPortgroupInfo from a JSON string"""
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
        """Create an instance of DistributedVirtualPortgroupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


