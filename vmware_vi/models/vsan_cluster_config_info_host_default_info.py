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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VsanClusterConfigInfoHostDefaultInfo(DataObject):
    """
    Default VSAN service configuration to be used for hosts admitted to the cluster.  See also *VsanClusterConfigInfo.defaultConfig*.  ***Since:*** vSphere API 5.5 
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="VSAN service cluster UUID, in the string form \"nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn\", where n are hexadecimal digits.  When enabling the VSAN service on the cluster, this value shall not be specified by the user; a suitable UUID will be generated by the platform. While the VSAN service is enabled, this is a read-only value.  ***Since:*** vSphere API 5.5 ")
    auto_claim_storage: Optional[StrictBool] = Field(default=None, description="Deprecated as this configuration will be deprecated, autoclaim will be no longer supported.  Whether the VSAN service is configured to automatically claim local storage on VSAN-enabled hosts in the cluster.  If omitted while enabling the VSAN service, this value will default to <code>true</code>. Changing this value to <code>false</code> shall not affect any existing disk mappings in use by hosts currently participating in the VSAN service. Changing this value to <code>true</code> will result in local disks being automatically claimed for use by the VSAN service, for hosts currently participating in the VSAN service.  See also *VsanHostConfigInfoStorageInfo.diskMapping*, *VsanHostConfigInfoStorageInfo.autoClaimStorage*.  ***Since:*** vSphere API 5.5 ", alias="autoClaimStorage")
    checksum_enabled: Optional[StrictBool] = Field(default=None, description="Whether the VSAN service is configured to enforce checksum protection.  If omitted while enabling the VSAN service, this value will default to <code>false<code>. Change this value to <code>false</code> shall not affect any existing disk status. Changing this value to <code>true</code> shall do disk enforcement check that all VSAN disks are checksum enabled.  ***Since:*** vSphere API 6.0 ", alias="checksumEnabled")
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
        """Create an instance of VsanClusterConfigInfoHostDefaultInfo from a JSON string"""
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
        """Create an instance of VsanClusterConfigInfoHostDefaultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


