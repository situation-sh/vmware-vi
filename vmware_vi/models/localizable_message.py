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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.key_any_value import KeyAnyValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LocalizableMessage(DataObject):
    """
    Message data which is intended to be displayed according to the locale of a client.  A *LocalizableMessage* contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.  Clients of the VIM API may use vim.SessionManager.setLocale() to cause the server to emit a localized *LocalizableMessage.message*, or may perform client-side localization based on message catalogs provided by the server. - If the substition variable is a string, no further lookup is required.   - *LocalizableMessage.arg* = \\[(\"address\" = \"127.0.0.1\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"IP address is {address}\"   - \\==&gt; *LocalizableMessage.message* = \"IP address is 127.0.0.1\" - If the substitution variable is an integer, value is a lookup key.   - *LocalizableMessage.arg* = \\[(\"1\" = \"button.cancel\"), (\"2\" = \"msg.revert\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"Select '{1}' to {2}\"   - CATALOG(locmsg, button.cancel) = \"Cancel\"   - CATALOG(locmsg, msg.revert) = \"revert\"   - \\==&gt; *LocalizableMessage.message* = \"Select 'Cancel' to revert\" - If the variable contains '@', value is a label lookup in another   catalog, where {name.@CATALOG.prefix} looks up prefix.*LocalizableMessage.arg*\\[name\\].label   in CATALOG.   - *LocalizableMessage.arg* = \\[(\"field\" = \"queued\")\\]   - CATALOG(locmsg, *LocalizableMessage.key*) = \"State is {field.@enum.TaskInfo.State}\"   - CATALOG(enum, TaskInfo.State.queued.label) is \"Queued\"   - \\==&gt; *LocalizableMessage.message* = \"State is Queued\"      ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: StrictStr = Field(description="Unique key identifying the message in the localized message catalog.  ***Since:*** vSphere API 4.0 ")
    arg: Optional[List[KeyAnyValue]] = Field(default=None, description="Substitution arguments for variables in the localized message.  ***Since:*** vSphere API 4.0 ")
    message: Optional[StrictStr] = Field(default=None, description="Message in session locale.  Use vim.SessionManager.setLocale() to change the session locale.  ***Since:*** vSphere API 4.0 ")
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
        """Create an instance of LocalizableMessage from a JSON string"""
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
        """Create an instance of LocalizableMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


