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
from vmware_vi.models.key_value import KeyValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HttpNfcLeaseSourceFile(DataObject):
    """
    Descriptor of the remote source file used in pull scenario.  ***Since:*** vSphere API 6.7 
    """ # noqa: E501
    target_device_id: StrictStr = Field(description="Target device id that will be used to store remote file.  Uniquely identifies host, vm and device. Given by this lease in *HttpNfcLeaseDeviceUrl.importKey*.  ***Since:*** vSphere API 6.7 ", alias="targetDeviceId")
    url: StrictStr = Field(description="Full url of the source file, for example https://server/path/disk-1.vmdk.  Or url to OVA, in that case *HttpNfcLeaseSourceFile.memberName* should be specified.  ***Since:*** vSphere API 6.7 ")
    member_name: Optional[StrictStr] = Field(default=None, description="Used only when OVA is specified in *HttpNfcLeaseSourceFile.url*.  Should contain file name to extract from OVA.  ***Since:*** vSphere API 6.7 ", alias="memberName")
    create: StrictBool = Field(description="True if PUT should be used for upload, otherwise POST.  Same as *OvfFileItem.create*  ***Since:*** vSphere API 6.7 ")
    ssl_thumbprint: Optional[StrictStr] = Field(default=None, description="Esx has no CA database for checking arbitrary certificates.  Client should verify the server certificate and provide certificate thumbprint here.  ***Since:*** vSphere API 6.7 ", alias="sslThumbprint")
    http_headers: Optional[List[KeyValue]] = Field(default=None, description="For the case when remote server requires authentication or any other type of custom HTTP headers be provided with the request.  ***Since:*** vSphere API 6.7 ", alias="httpHeaders")
    size: Optional[StrictInt] = Field(default=None, description="Size of the file, if known.  Otherwise it will be determined by a HEAD request. Not used for OVA members.  ***Since:*** vSphere API 6.7 ")
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
        """Create an instance of HttpNfcLeaseSourceFile from a JSON string"""
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
        """Create an instance of HttpNfcLeaseSourceFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


