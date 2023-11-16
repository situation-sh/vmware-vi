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
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.guest_file_attributes import GuestFileAttributes
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FileTransferInformation(DataObject):
    """
    Represents the information about a *GuestFileManager.InitiateFileTransferFromGuest* operation of *GuestFileManager* object.  The user can use the URL provided in url property to transfer the file from the guest. The user should send a HTTP GET request to the URL. Entire file content will be returned in the body of the response message.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    attributes: GuestFileAttributes
    size: StrictInt = Field(description="Total size of the file in bytes.  ***Since:*** vSphere API 5.0 ")
    url: StrictStr = Field(description="Specifies the URL to which the user has to send HTTP GET request.  Multiple GET requests cannot be sent to the URL simultaneously. URL will become invalid once a successful GET request is sent.       The host part of the URL is returned as '\\*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file is available for download from `https://esx-svr-1.domain1.com/guestFile?id=1&token=1234`, the URL returned may be `https://&#42;/guestFile?id=1&token=1234`. The client replaces the asterisk with the server name on which it invoked the call.       The URL is valid only for 10 minutes from the time it is generated. Also, the URL becomes invalid whenever the virtual machine is powered off, suspended or unregistered.  ***Since:*** vSphere API 5.0 ")
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
        """Create an instance of FileTransferInformation from a JSON string"""
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
        """Create an instance of FileTransferInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

