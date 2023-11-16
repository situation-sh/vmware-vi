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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RetrieveUserGroupsRequestType(BaseModel):
    """
    The parameters of *UserDirectory.RetrieveUserGroups*. 
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description="Domain to be searched. If not set, then the method searches the local machine. ")
    search_str: StrictStr = Field(description="Case insensitive substring used to filter results; the search string is compared to the login and full name for users, and the name and description for groups. Leave this blank to match all users. ", alias="searchStr")
    belongs_to_group: Optional[StrictStr] = Field(default=None, description="If present, the returned list contains only users or groups that directly belong to the specified group. Users or groups that have indirect membership will not be included in the list. ", alias="belongsToGroup")
    belongs_to_user: Optional[StrictStr] = Field(default=None, description="If present, the returned list contains only groups that directly contain the specified user. Groups that indirectly contain the user will not be included in the list. ", alias="belongsToUser")
    exact_match: StrictBool = Field(description="Indicates the searchStr passed should match a user or group name exactly. ", alias="exactMatch")
    find_users: StrictBool = Field(description="True, if users should be included in the result. ", alias="findUsers")
    find_groups: StrictBool = Field(description="True, if groups should be included in the result. ", alias="findGroups")
    __properties: ClassVar[List[str]] = ["domain", "searchStr", "belongsToGroup", "belongsToUser", "exactMatch", "findUsers", "findGroups"]

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
        """Create an instance of RetrieveUserGroupsRequestType from a JSON string"""
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
        """Create an instance of RetrieveUserGroupsRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "searchStr": obj.get("searchStr"),
            "belongsToGroup": obj.get("belongsToGroup"),
            "belongsToUser": obj.get("belongsToUser"),
            "exactMatch": obj.get("exactMatch"),
            "findUsers": obj.get("findUsers"),
            "findGroups": obj.get("findGroups")
        })
        return _obj


