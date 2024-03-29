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

class HostNicFailureCriteria(DataObject):
    """
    This data object type describes the network adapter failover detection algorithm for a network adapter team. 
    """ # noqa: E501
    check_speed: Optional[StrictStr] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  To use link speed as the criteria, _checkSpeed_ must be one of the following values: - **exact**: Use exact speed to detect link failure.   **speed** is the configured exact speed in megabits per second. - **minimum**: Use minimum speed to detect failure.   **speed** is the configured minimum speed in megabits per second. - **empty string**: Do not use link speed to detect failure.   **speed** is unused in this case. ", alias="checkSpeed")
    speed: Optional[StrictInt] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  Speed.  See also *HostNicFailureCriteria.checkSpeed*. ")
    check_duplex: Optional[StrictBool] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  The flag to indicate whether or not to use the link duplex reported by the driver as link selection criteria.  If **checkDuplex** is true, then fullDuplex is the configured duplex mode. The link is considered bad if the link duplex reported by driver is not the same as fullDuplex.  If **checkDuplex** is false, then fullDuplex is unused, and link duplexity is not used as a detection method. ", alias="checkDuplex")
    full_duplex: Optional[StrictBool] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  Full duplex.  See also *HostNicFailureCriteria.checkDuplex*. ", alias="fullDuplex")
    check_error_percent: Optional[StrictBool] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  The flag to indicate whether or not to use link error percentage to detect failure.  If **checkErrorPercent** is true, then percentage is the configured error percentage that is tolerated. The link is considered bad if error rate exceeds percentage.  If **checkErrorPercent** is false, percentage is unused, and error percentage is not used as a detection method. ", alias="checkErrorPercent")
    percentage: Optional[StrictInt] = Field(default=None, description="Deprecated as of VI API 5.1, this property is not supported.  Percentage.  See also *HostNicFailureCriteria.checkErrorPercent*. ")
    check_beacon: Optional[StrictBool] = Field(default=None, description="The flag to indicate whether or not to enable this property to enable beacon probing as a method to validate the link status of a physical network adapter.  **checkBeacon** can be enabled only if the VirtualSwitch has been configured to use the beacon. Attempting to set **checkBeacon** on a PortGroup or VirtualSwitch that does not have beacon probing configured for the applicable VirtualSwitch results in an error.  See also *HostVirtualSwitchBondBridge.beacon*, *HostVirtualSwitchBeaconConfig*. ", alias="checkBeacon")
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
        """Create an instance of HostNicFailureCriteria from a JSON string"""
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
        """Create an instance of HostNicFailureCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


