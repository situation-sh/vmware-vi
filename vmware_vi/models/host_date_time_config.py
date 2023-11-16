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
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_ntp_config import HostNtpConfig
from vmware_vi.models.host_ptp_config import HostPtpConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostDateTimeConfig(DataObject):
    """
    This data object represents the dateTime configuration of the host.  ***Since:*** VI API 2.5 
    """ # noqa: E501
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone of the host.  Must be one of the values of *HostDateTimeSystemTimeZone.key*  ***Since:*** VI API 2.5 ", alias="timeZone")
    ntp_config: Optional[HostNtpConfig] = Field(default=None, alias="ntpConfig")
    ptp_config: Optional[HostPtpConfig] = Field(default=None, alias="ptpConfig")
    protocol: Optional[StrictStr] = Field(default=None, description="Specify which network time configuration to discipline vmkernel clock.  See *HostDateTimeInfoProtocol_enum* for supported values.  ***Since:*** vSphere API 7.0.3.0 ")
    enabled: Optional[StrictBool] = Field(default=None, description="Bring Time services subsystem up or down.  ***Since:*** vSphere API 7.0.3.0 ")
    disable_events: Optional[StrictBool] = Field(default=None, description="When Network Time service or Precision Time service are enabled any detecteced failures will result in Events being sent to Virtual Center.  Use this setting to disable Time Events.  ***Since:*** vSphere API 7.0.3.0 ", alias="disableEvents")
    disable_fallback: Optional[StrictBool] = Field(default=None, description="When in PrecisionTimeSync, NTP configuration as set will be running as backup.  Use this setting to prevent NTP from becoming the primary time protocol in the event of a PTP service failure.  ***Since:*** vSphere API 7.0.3.0 ", alias="disableFallback")
    reset_to_factory_defaults: Optional[StrictBool] = Field(default=None, description="When this property is present and set true the existing configuration for Time Services will be reset to factory default.  The protocol property when set defines the scope of what is reset. If additional configuration beyond protocol is provided host will first perform factory reset followed by applying any configuration present.  ***Since:*** vSphere API 7.0.3.0 ", alias="resetToFactoryDefaults")
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
        """Create an instance of HostDateTimeConfig from a JSON string"""
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
        """Create an instance of HostDateTimeConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

