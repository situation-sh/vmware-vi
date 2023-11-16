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
from pydantic import SecretStr, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostPatchManagerPatchManagerOperationSpec(DataObject):
    """
    Optional parameters for hostd to pass to exupdate.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    proxy: Optional[StrictStr] = Field(default=None, description="The name of the possible proxy for esxupdate to use to connect to a server.  The patch and metadata may be cached within the proxy server.  ***Since:*** vSphere API 4.0 ")
    port: Optional[StrictInt] = Field(default=None, description="The port of the possible proxy for esxupdate to use to connect to a server.  The patch and metadata may be cached within the proxy server.  ***Since:*** vSphere API 4.0 ")
    user_name: Optional[StrictStr] = Field(default=None, description="The user name used for the proxy server.  ***Since:*** vSphere API 4.0 ", alias="userName")
    password: Optional[SecretStr] = Field(default=None, description="The password used for the proxy server.  This is passed with ssl through a trusted channel.  ***Since:*** vSphere API 4.0 ")
    cmd_option: Optional[StrictStr] = Field(default=None, description="Possible command line options when calling esxupdate.  ***Since:*** vSphere API 4.0 ", alias="cmdOption")
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
        """Create an instance of HostPatchManagerPatchManagerOperationSpec from a JSON string"""
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
        """Create an instance of HostPatchManagerPatchManagerOperationSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

