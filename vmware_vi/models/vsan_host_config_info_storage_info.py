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
from vmware_vi.models.vsan_host_disk_map_info import VsanHostDiskMapInfo
from vmware_vi.models.vsan_host_disk_mapping import VsanHostDiskMapping
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VsanHostConfigInfoStorageInfo(DataObject):
    """
    Host-local VSAN storage configuration.  This data object is used both for specifying and retrieving storage configuration for a host participating in the VSAN service.  ***Since:*** vSphere API 5.5 
    """ # noqa: E501
    auto_claim_storage: Optional[StrictBool] = Field(default=None, description="Deprecated as this configuration will be deprecated, autoclaim will be no longer supported.  Whether the VSAN service is configured to automatically claim local unused storage on this host.  When set, the VSAN service will automatically format and use local disks. Side effects from any disk consumption will be reflected in *VsanHostConfigInfoStorageInfo.diskMapping*. If this argument is specified as a host-level configuration input at the VC-level (see *ClusterConfigInfoEx.vsanHostConfig*), it will override that of any cluster-level default value.  See also *VsanHostConfigInfoStorageInfo.diskMapping*, *ClusterConfigInfoEx.vsanHostConfig*, *VsanClusterConfigInfo.defaultConfig*.  ***Since:*** vSphere API 5.5 ", alias="autoClaimStorage")
    disk_mapping: Optional[List[VsanHostDiskMapping]] = Field(default=None, description="Deprecated use *VsanHostConfigInfoStorageInfo.diskMapInfo* instead.  List of *VsanHostDiskMapping* entries in use by the VSAN service.  DiskMappings to be used by the VSAN service may be manually specified using *HostVsanSystem.InitializeDisks_Task*.  See also *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 5.5 ", alias="diskMapping")
    disk_map_info: Optional[List[VsanHostDiskMapInfo]] = Field(default=None, description="List of *VsanHostDiskMapping* entries with runtime information from the perspective of this host.  ***Since:*** vSphere API 6.0 ", alias="diskMapInfo")
    checksum_enabled: Optional[StrictBool] = Field(default=None, description="Deprecated this attribute was originally used for indicating whether hardware checksums is supported on the disks. But in vSphere 2016 hardware checksums are replaced with software implementation, supported by all disks. This makes current field redundant, and its value as an input/output is ignored.  Whether checksum is enabled on all the disks in this host.  If any disk is not checksum capable or 520 bps formatted, we will skip it.  ***Since:*** vSphere API 6.0 ", alias="checksumEnabled")
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
        """Create an instance of VsanHostConfigInfoStorageInfo from a JSON string"""
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
        """Create an instance of VsanHostConfigInfoStorageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


