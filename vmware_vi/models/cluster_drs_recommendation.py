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


from typing import Any, ClassVar, Dict, List
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.cluster_drs_migration import ClusterDrsMigration
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterDrsRecommendation(DataObject):
    """
    Deprecated as of VI API 2.5 use *ClusterRecommendation*.  DrsRecommendation describes a recommendation to migrate one or more virtual machines. 
    """ # noqa: E501
    key: StrictStr = Field(description="Key to identify the recommendation when calling applyRecommendation. ")
    rating: StrictInt = Field(description="A rating of the recommendation.  Valid values range from 1 (lowest confidence) to 5 (highest confidence). ")
    reason: StrictStr = Field(description="A reason code explaining why this set of migrations is being suggested. ")
    reason_text: StrictStr = Field(description="Text that provides more information about the reason code for the suggested set of migrations. ", alias="reasonText")
    migration_list: List[ClusterDrsMigration] = Field(description="Deprecated a more general *recommendation* list should be used. This recommendation type and the migrationList is kept for backward compatibility.  List of migrations in this recommendation and all the parent recommendations on which this recommendation depends.  All the migrations in this list can be constructed from *ClusterRecommendation.prerequisite* and *ClusterRecommendation.action*. ", alias="migrationList")
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
        """Create an instance of ClusterDrsRecommendation from a JSON string"""
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
        """Create an instance of ClusterDrsRecommendation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


