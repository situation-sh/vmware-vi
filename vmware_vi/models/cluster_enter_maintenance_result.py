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
from vmware_vi.models.cluster_drs_faults import ClusterDrsFaults
from vmware_vi.models.cluster_recommendation import ClusterRecommendation
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterEnterMaintenanceResult(DataObject):
    """
    EnterMaintenanceResult is the base class of the result returned to the *ClusterComputeResource.ClusterEnterMaintenanceMode* method.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    recommendations: Optional[List[ClusterRecommendation]] = Field(default=None, description="The list of recommendations for hosts that Virtual Center will be able to evacuate.  Each recommendation consists of a host maintenance action *ClusterAction* for a host, along with zero or more vmotions for evacuation. Application of the recommendations is not supported currently. The client will have to put the hosts into maintenance mode by calling the separate method *HostSystem.EnterMaintenanceMode_Task*.  ***Since:*** vSphere API 5.0 ")
    fault: Optional[ClusterDrsFaults] = None
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
        """Create an instance of ClusterEnterMaintenanceResult from a JSON string"""
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
        """Create an instance of ClusterEnterMaintenanceResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


