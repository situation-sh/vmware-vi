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
from pydantic import BaseModel, SecretStr, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryConnectionInfoRequestType(BaseModel):
    """
    The parameters of *Datacenter.QueryConnectionInfo*. 
    """ # noqa: E501
    hostname: StrictStr = Field(description="The target of the query. ")
    port: StrictInt = Field(description="The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports. ")
    username: StrictStr = Field(description="The name of the user. ")
    password: SecretStr = Field(description="The password of the user. ")
    ssl_thumbprint: Optional[StrictStr] = Field(default=None, description="The expected SSL thumbprint of the host's certificate. ", alias="sslThumbprint")
    __properties: ClassVar[List[str]] = ["hostname", "port", "username", "password", "sslThumbprint"]

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
        """Create an instance of QueryConnectionInfoRequestType from a JSON string"""
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
        """Create an instance of QueryConnectionInfoRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostname": obj.get("hostname"),
            "port": obj.get("port"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "sslThumbprint": obj.get("sslThumbprint")
        })
        return _obj


