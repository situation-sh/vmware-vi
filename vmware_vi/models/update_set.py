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
from vmware_vi.models.property_filter_update import PropertyFilterUpdate
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateSet(DataObject):
    """
    A set of updates that represent the changes since a prior call to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx*. 
    """ # noqa: E501
    version: StrictStr = Field(description="New data version to pass in the next call to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx*.  These versions, although they are opaque, are strongly ordered in the sense that passing a version to *PropertyCollector.WaitForUpdates*, *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdatesEx* requests updates that reflect changes in the objects selected by the Filter that happened after the specified version. ")
    filter_set: Optional[List[PropertyFilterUpdate]] = Field(default=None, description="Set of managed object updates detected by specific filters.  Updates are reported in sets. Each set is associated with a reference to a filter that detected the updates in the set. ", alias="filterSet")
    truncated: Optional[StrictBool] = Field(default=None, description="If true, this *UpdateSet* contains results from a suspended change calculation, which places restrictions on the use of version.  The *PropertyCollector* may suspend a calculation due to server policy or if the total number of *ObjectUpdate* entries summed across every *PropertyFilterUpdate* reached the maximum specified in *WaitOptions.maxObjectUpdates*. The client can pass the \"truncated data version\" to *PropertyCollector.WaitForUpdatesEx* to resume the update calculation, which will start on the filter where it left off. A truncated data version cannot be used more than once and may not be passed to *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates*. *UpdateSet.truncated* will never be true in an *UpdateSet* returned from *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates*.  If false, this *UpdateSet* contains a complete change calculation or the last part of a series of suspended change calculations. The version may be passed to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx* more than once. Re-using a version allows a client to recover a change sequence after a transient failure on a previous call.  ***Since:*** vSphere API 4.1 ")
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
        """Create an instance of UpdateSet from a JSON string"""
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
        """Create an instance of UpdateSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

