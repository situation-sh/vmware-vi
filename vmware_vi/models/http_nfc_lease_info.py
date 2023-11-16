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
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.http_nfc_lease_datastore_lease_info import HttpNfcLeaseDatastoreLeaseInfo
from vmware_vi.models.http_nfc_lease_device_url import HttpNfcLeaseDeviceUrl
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HttpNfcLeaseInfo(DataObject):
    """
    This class holds information about the lease, such as the entity covered by the lease, and HTTP URLs for up/downloading file backings.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    lease: ManagedObjectReference
    entity: ManagedObjectReference
    device_url: Optional[List[HttpNfcLeaseDeviceUrl]] = Field(default=None, description="The deviceUrl property contains a mapping from logical device keys to URLs.  ***Since:*** vSphere API 4.0 ", alias="deviceUrl")
    total_disk_capacity_in_kb: StrictInt = Field(description="Total capacity in kilobytes of all disks in all Virtual Machines covered by this lease.  This can be used to track progress when transferring disks.  ***Since:*** vSphere API 4.0 ", alias="totalDiskCapacityInKB")
    lease_timeout: StrictInt = Field(description="Number of seconds before the lease times out.  The client extends the lease by calling *HttpNfcLease.HttpNfcLeaseProgress* before the timeout has expired.  ***Since:*** vSphere API 4.0 ", alias="leaseTimeout")
    host_map: Optional[List[HttpNfcLeaseDatastoreLeaseInfo]] = Field(default=None, description="Map of URLs for leased hosts for a given datastore.  This is used to look up multi-POST-capable hosts for a datastore.  ***Since:*** vSphere API 4.1 ", alias="hostMap")
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
        """Create an instance of HttpNfcLeaseInfo from a JSON string"""
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
        """Create an instance of HttpNfcLeaseInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


