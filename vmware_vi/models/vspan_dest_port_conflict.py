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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.dvs_fault import DvsFault
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VspanDestPortConflict(DvsFault):
    """
    Thrown if a dvPort is used as destination in multiple Distributed Port Mirroring sessions.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    vspan_session_key1: StrictStr = Field(description="The key of the Distributed Port Mirroring session whose destination ports include a port that is also used as destination ports of other Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0 ", alias="vspanSessionKey1")
    vspan_session_key2: StrictStr = Field(description="The key of the Distributed Port Mirroring session whose destination ports include a port that is also used as destination ports of other Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0 ", alias="vspanSessionKey2")
    port_key: StrictStr = Field(description="The key of the the port that is used as destination in multiple Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0 ", alias="portKey")
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
        """Create an instance of VspanDestPortConflict from a JSON string"""
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
        """Create an instance of VspanDestPortConflict from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

