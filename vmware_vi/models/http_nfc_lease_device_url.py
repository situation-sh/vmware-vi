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

class HttpNfcLeaseDeviceUrl(DataObject):
    """
    Provides a mapping from logical device IDs to upload/download URLs.  For export, a single device id is returned based on the object identifiers for the objects.  For import, two device ids are returned. One based on the object names used in the ImportSpec, and one based on the object identifiers for the created objects. This is immutable and would match the id if an ExportLease is latter created.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: StrictStr = Field(description="The immutable identifier for the device.  This is set for both import/export leases.  ***Since:*** vSphere API 4.0 ")
    import_key: StrictStr = Field(description="Identifies the device based on the names in an ImportSpec.  This is only set for import leases.  ***Since:*** vSphere API 4.0 ", alias="importKey")
    url: StrictStr
    ssl_thumbprint: StrictStr = Field(description="SSL thumbprint for the host the URL refers to.  Empty if no SSL thumbprint is available or needed.  ***Since:*** vSphere API 4.0 ", alias="sslThumbprint")
    disk: Optional[StrictBool] = Field(default=None, description="Optional value to specify if the attached file is a disk in vmdk format.  ***Since:*** vSphere API 4.1 ")
    target_id: Optional[StrictStr] = Field(default=None, description="Id for this target.  This only used for multi-POSTing, where a single HTTP POST is applied to multiple targets.  ***Since:*** vSphere API 4.1 ", alias="targetId")
    datastore_key: Optional[StrictStr] = Field(default=None, description="Key for the datastore this disk is on.  This is used to look up hosts which can be used to multi-POST disk contents, in the host map of the lease.  ***Since:*** vSphere API 4.1 ", alias="datastoreKey")
    file_size: Optional[StrictInt] = Field(default=None, description="Specifies the size of the file backing for this device.  This property is only set for non-disk file backings.  ***Since:*** vSphere API 4.1 ", alias="fileSize")
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
        """Create an instance of HttpNfcLeaseDeviceUrl from a JSON string"""
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
        """Create an instance of HttpNfcLeaseDeviceUrl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


