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
from pydantic import StrictBool
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.object_spec import ObjectSpec
from vmware_vi.models.property_spec import PropertySpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PropertyFilterSpec(DataObject):
    """
    Specify the property data that is included in a filter.  A filter can specify part of a single managed object, or parts of multiple related managed objects in an inventory hierarchy - for example, to collect updates from all virtual machines in a given folder. 
    """ # noqa: E501
    prop_set: List[PropertySpec] = Field(description="Set of properties to include in the filter, specified for each object type. ", alias="propSet")
    object_set: List[ObjectSpec] = Field(description="Set of specifications that determine the objects to filter. ", alias="objectSet")
    report_missing_objects_in_results: Optional[StrictBool] = Field(default=None, description="Control how to report missing objects during filter creation.  If false or unset and *PropertyFilterSpec.objectSet* refers to missing objects, filter creation will fail with a *ManagedObjectNotFound* fault.  If true and *PropertyFilterSpec.objectSet* refers to missing objects, filter creation will not fail and missing objects will be reported via filter results. This is the recommended setting when *PropertyFilterSpec.objectSet* refers to transient objects.  In an *UpdateSet* missing objects will appear in the *PropertyFilterUpdate.missingSet* field.  In a *RetrieveResult* missing objects will simply be omitted from the objects field.  For a call to *PropertyCollector.RetrieveProperties* missing objects will simply be omitted from the results.  ***Since:*** vSphere API 4.1 ", alias="reportMissingObjectsInResults")
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
        """Create an instance of PropertyFilterSpec from a JSON string"""
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
        """Create an instance of PropertyFilterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

