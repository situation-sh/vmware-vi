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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.customization_identity_settings import CustomizationIdentitySettings
from vmware_vi.models.customization_name import CustomizationName
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomizationLinuxPrep(CustomizationIdentitySettings):
    """
    This is the Linux counterpart to the Windows Sysprep object.  LinuxPrep contains machine-wide settings that identify a Linux machine in the same way that the Sysprep type identifies a Windows machine. 
    """ # noqa: E501
    host_name: CustomizationName = Field(alias="hostName")
    domain: StrictStr = Field(description="The fully qualified domain name. ")
    time_zone: Optional[StrictStr] = Field(default=None, description="The case-sensitive timezone, such as Europe/Sofia.  <a href=\"timezone.html\"title=\"Display list of Valid timeZone values...\"> **Valid timeZone values**</a> are based on the tz (timezone) database used by Linux and other Unix systems. The values are strings (xsd:string) in the form \"Area/Location,\" in which Area is a continent or ocean name, and Location is the city, island, or other regional designation.  See the <a href=\"https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2145518\"target=\"_blank\">List of supported time zones for different vSphere versions in Linux/Unix systems</a>.  ***Since:*** vSphere API 4.0 ", alias="timeZone")
    hw_clock_utc: Optional[StrictBool] = Field(default=None, description="Specifies whether the hardware clock is in UTC or local time. - True when the hardware clock is in UTC. - False when the hardware clock is in local time.    ***Since:*** vSphere API 4.0 ", alias="hwClockUTC")
    script_text: Optional[StrictStr] = Field(default=None, description="The script to run before and after GOS customization.  ***Since:*** vSphere API 7.0 ", alias="scriptText")
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
        """Create an instance of CustomizationLinuxPrep from a JSON string"""
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
        """Create an instance of CustomizationLinuxPrep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


